import ctypes
import os
import serial
import logging
import time
import socket
import serial.tools.list_ports
try:
    from APP.logger import log_message
except ImportError:
    from logger import log_message
# 打印机的Vendor ID和Product ID，需要根据实际打印机的设备进行修改
VENDOR_ID =  0x0FE6
PRODUCT_ID = 0x811E

class Dll_Init:
    def __init__(self):
        self.Dll_path = "null"
        self.Dll_Flag = 0
        self.buffer_size = 256
        self.buffer_usb = "null"
        self.buffer_serial = "null"
        self.res_buffer = ""
        self.Port_result = 0
        ret = self.Getdll_path()
        if ret :
            self.Join_dll()
        else :
            pass
        #网口信息
        self.client_socket = None
        self.socket_ip = None
        self.socket_port = None
        self.connected = False
    def Getdll_path(self):
        APP_DIR = os.getcwd()
       # MAIN_DIR = os.path.dirname(APP_DIR)
        DLL_Name = r"DLL\CsnPrinterLibs.dll"

        self.Dll_path = os.path.join(APP_DIR, DLL_Name)
        if os.path.exists(self.Dll_path):
            self.Dll_Flag = 1
            return 1
        else :
            log = "没有找到共享库的路径; 当前路径:{}".format(self.Dll_path)
            log_message(log,logging.WARNING)
            return 0
    #加载库
    def Join_dll(self):
        self.mylib = ctypes.CDLL(self.Dll_path)
        #USB 的接口
        self.mylib.Port_EnumUSB.argtypes = [ctypes.c_char_p, ctypes.c_size_t]
        self.mylib.Port_EnumUSB.restype = ctypes.c_size_t
        self.mylib.Port_OpenUSBIO.argtypes = [ctypes.c_char_p]
        self.mylib.Port_OpenUSBIO.restype = ctypes.c_void_p
        self.mylib.Port_SetPort.argtypes = [ctypes.c_void_p]
        self.mylib.Port_SetPort.restype = ctypes.c_bool
        self.mylib.Port_ClosePort.argtypes = [ctypes.c_void_p]
        self.mylib.Pos_SelfTest.restype = ctypes.c_bool
        self.buffer_usb = ctypes.create_string_buffer(self.buffer_size)
        self.mylib.WriteData.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.c_size_t, ctypes.c_ulong]
        self.mylib.WriteData.restype = ctypes.c_int
        #USB写入
        self.mylib.Read.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.c_size_t, ctypes.c_ulong]
        self.mylib.Read.restype = ctypes.c_int
        #串口 的接口
        self.mylib.Port_EnumCOM.argtypes = [ctypes.c_char_p, ctypes.c_size_t]
        self.mylib.Port_EnumCOM.restype = ctypes.c_size_t
        self.buffer_serial = ctypes.create_string_buffer(self.buffer_size)
        #打印二维码
        self.mylib.Pos_Qrcode.argtypes = [ctypes.c_wchar_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]
        self.mylib.Pos_Qrcode.restype = ctypes.c_bool
        #打印图片
        self.mylib.Pos_ImagePrint.argtypes = [ctypes.c_wchar_p, ctypes.c_int, ctypes.c_int]
        self.mylib.Pos_ImagePrint.restype = ctypes.c_bool       
    #列出USB接口
    def list_usb_devices(self):
        if not self.Dll_Flag :
            return []
        ctypes.memset(self.buffer_usb, 0, self.buffer_size)
        result_length = self.mylib.Port_EnumUSB(self.buffer_usb, self.buffer_size)
        buffer_bytes = self.buffer_usb.raw
        # 如果需要替换零字节并显示处理后的数据
        usb_devices = buffer_bytes.split(b'\0')
        usb_devices = [device.decode('utf-8', errors='replace') for device in usb_devices if device]
        return usb_devices
    
    #打开Usb接口
    def Open_UsbCom(self):
        if not self.Dll_Flag :
            return 0
        self.res_buffer = self.mylib.Port_OpenUSBIO(self.buffer_usb)  
        if not self.res_buffer :
            return 0      
        self.Port_result = self.mylib.Port_SetPort(self.res_buffer)  
        if not self.Port_result :
            return 0
        return 1
    def Write_Usbdata(self,data):
        if isinstance(data, str):
            encoded_data = data.encode('cp936')
        else :
            encoded_data = data
        buf =  ctypes.create_string_buffer(bytes(encoded_data))  # 创建字符串缓冲区
        count =  ctypes.c_size_t(len(encoded_data))  # 数据长度
        timeout = ctypes.c_ulong(5000)  # 超时设置（例如 5000 毫秒）
        buf_ptr = ctypes.cast(buf, ctypes.POINTER(ctypes.c_ubyte))
        result = self.mylib.WriteData(buf_ptr, count, timeout)
        return result
    
    def Read_Usbdata(self,buttf_size=1024):
        buf =  ctypes.create_string_buffer(buttf_size)  # 创建字符串缓冲区
        count =  ctypes.c_size_t(buttf_size)
        timeout = ctypes.c_ulong(2)  # 超时设置（例如 5000 毫秒）
        buf_ptr2 = ctypes.cast(buf, ctypes.POINTER(ctypes.c_ubyte))
        self.mylib.ReadInit()
        result = self.mylib.ReadData(buf_ptr2, count, timeout)
        
        data_str = b''
        if result > 0:
            data_str = buf.raw[:result]
            hex_representation = ' '.join(f'{byte:02X}' for byte in data_str)  # 转换为十六进制字符串
        else:
            hex_representation = 0xFF
            log = "没有读取到打印机返回的数据"
            log_message(log,logging.WARNING)

        return hex_representation

    def Close_ReadUsbData(self):
        self.mylib.ReadClose()

    def Close_UsbCom(self):
        if not self.Dll_Flag :
            return 0
        if self.Port_result:
            log = "关闭USB端口"
            log_message(log,logging.DEBUG)
            self.Port_result = self.mylib.Port_ClosePort(self.res_buffer) 
            self.Port_result = 0 
            return 1
    
    #列出串口接口
    def list_serial_com(self):
        if not self.Dll_Flag :
            ports = serial.tools.list_ports.comports()
            available_ports = [port.device for port in ports]
            return available_ports
        ctypes.memset(self.buffer_serial, 0, self.buffer_size)
        result_length = self.mylib.Port_EnumCOM(self.buffer_serial, self.buffer_size)
        buffer_bytes = self.buffer_serial.raw
        # 如果需要替换零字节并显示处理后的数据
        serial_devices = buffer_bytes.split(b'\0')
        serial_devices = [device.decode('utf-8', errors='replace') for device in serial_devices if device]
        return serial_devices
        
    
    def Open_serialCom(self,port, baudrate):
        try:
            self.ser = serial.Serial(port, baudrate, timeout=2)
            return 1
        except serial.SerialException as e:
            log = "打开串口失败: {}".format(e)
            log_message(log,logging.ERROR)
            return 0
        except Exception as e:
            log = "发生其他错误: {}".format(e)
            log_message(log,logging.ERROR)
            return 0
        
    def Write_serialCom(self,data):
        log = None
        try:
            if not self.ser.is_open:
                log = "串口未打开或断开，正重新打开..."
                log_message(log,logging.WARNING)
                self.ser.open()    
            if isinstance(data, str):
                 encoded_data = data.encode('cp936')
            else :
                 encoded_data = data 
            result = self.ser.write(encoded_data)
            log = ">>>>>> 任务发送成功，返回：{}  <<<<<<".format(result)
            log_message(log,logging.DEBUG)
        except serial.SerialException as e:
            log = "串口错误：{}".format(e)
            log_message(log,logging.ERROR)
            if self.ser.is_open:
                self.ser.close()
        except Exception as e:
            log = "发生错误{}".format(e)
            log_message(log,logging.ERROR)
            if self.ser.is_open:
                self.ser.close()


    def Close_serialCom(self):
        # 关闭串口
        if self.ser.is_open:
            log = "关闭串口"
            log_message(log,logging.DEBUG)
            self.ser.close()
    #网口通信

    #打开网口
    def Open_EthernetTcp(self,server_ip,server_port):
        # 创建 TCP 套接字并连接到服务器
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.settimeout(2)
        #ip地址
        self.socket_ip = server_ip
        self.socket_port = server_port
        print(f"IP= {self.socket_ip},Port={self.socket_port}")
        try:
            self.client_socket.connect((self.socket_ip, self.socket_port))
            log = "连接成功"
            self.connected = True
        except Exception as e:
            log = "错误", "连接失败:  {}".format(e)
            log_message(log,logging.ERROR)
            return False
        return True
    #网口写入数据
    def Write_EthernetTcp(self,data):
        try:
            ret = self.client_socket.sendall(data)
            log = ">>>>>> 任务发送成功，返回：{}  <<<<<<".format(ret)
            log_message(log,logging.DEBUG)
        except Exception as e:
            log = "网络错误：发送数据失败{}".format(e)
            log_message(log,logging.ERROR)

    #网口读取数据
    def Read_EthernetTcp(self):
        pass
    #网口关闭
    def Close_EthernetTcp(self):
        # 关闭套接字并退出
        if self.connected:
            self.client_socket.close()
            self.connected = False
            log = "关闭网络连接"
            log_message(log,logging.DEBUG)


    def Print_selfTest(self):
        ret = self.mylib.Pos_SelfTest()
        return ret 
    #打印二位码
    def Print_QRCode(self,QrcodeData,nWidth = 2,nVersion = 0,nErrlevenl = 4):
        ret = self.mylib.Pos_Qrcode(QrcodeData,nWidth,nVersion,nErrlevenl)
        return ret
    
    def Print_Image(self,Image_path,nWidth = 384,nBinaryAlgorithm=0):
        ret = self.mylib.Pos_ImagePrint(Image_path,nWidth,nBinaryAlgorithm)
        return ret
    #打印12.5%票据速度
    def Print_SpeedData(self,Data,ComType):
        if ComType == "串口":
            self.Write_serialCom(Data)
        elif ComType == "USB":
            self.Write_Usbdata(Data)
        else :
            pass
Comm_class = Dll_Init()
if __name__ == "__main__":

    Usb_devices = Comm_class.list_usb_devices()

    if  Usb_devices:
        print("找到的USB设备:", Usb_devices)
    else :
        print("没有找到设备")

    Comm_class.list_serial_com()
    Comm_class.Open_UsbCom()
    

    Comm_class.Read_Usbdata()
        #time.sleep(0.5)
    Comm_class.Close_UsbCom()    