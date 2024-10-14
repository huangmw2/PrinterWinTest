import usb.core
import usb.util
import ctypes
import os
import serial
import serial.tools.list_ports
import logging
try:
    from APP.Log import log_message
except ImportError:
    from Log import log_message
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
        #串口 的接口
        self.mylib.Port_EnumCOM.argtypes = [ctypes.c_char_p, ctypes.c_size_t]
        self.mylib.Port_EnumCOM.restype = ctypes.c_size_t
        self.buffer_serial = ctypes.create_string_buffer(self.buffer_size)
        #打印二维码
        self.mylib.Pos_Qrcode.argtypes = [ctypes.c_wchar_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]
        self.mylib.Pos_Qrcode.restype = ctypes.c_bool
    #列出USB接口
    def List_UsbCom(self):
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
            encoded_data = data.encode('utf-8')
        else :
            encoded_data = data
        buf =  ctypes.create_string_buffer(bytes(encoded_data))  # 创建字符串缓冲区
        count =  ctypes.c_size_t(len(encoded_data))  # 数据长度
        timeout = ctypes.c_ulong(5000)  # 超时设置（例如 5000 毫秒）
        buf_ptr = ctypes.cast(buf, ctypes.POINTER(ctypes.c_ubyte))
        result = self.mylib.WriteData(buf_ptr, count, timeout)
        return result
    
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
    def List_SerialCom(self):
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
        
        pass
    
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
                 encoded_data = data.encode('utf-8')
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

    def Print_selfTest(self):
        ret = self.mylib.Pos_SelfTest()
        return ret 
    #打印二位码
    def Print_QRCode(self,QrcodeData,nWidth = 2,nVersion = 0,nErrlevenl = 4):
        ret = self.mylib.Pos_Qrcode(QrcodeData,nWidth,nVersion,nErrlevenl)
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

    Usb_devices = Comm_class.List_UsbCom()

    if  Usb_devices:
        print("找到的USB设备:", Usb_devices)
    else :
        print("没有找到设备")

    Comm_class.List_SerialCom()