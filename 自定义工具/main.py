
#从库导入
import logging
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
#从其他模块导入
from APP.speed_test import Speed_Test
from APP.quality_checker import Quality_Test
from APP.printer_drive import Driver_Test
from APP.tspl_command import Tspl_Test
from APP.esc_command import Esc_Test
from APP.network_utils import Netword_Test
from APP.data_downloader import RAM_Test
from APP.param_config import Paras_Set
from APP.communication import Comm_class
from APP.queue_manager import queue_handler
from APP.logger import setup_logging, Rtn_logmessage,log_message, Clear_logfile
from APP.user_data import Config_Data




Global_Comtype = None

class StartUpWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("测试部自研工具")
        self.root.geometry("700x500+600+300")
        #绑定关闭窗口
        self.root.protocol("WM_DELETE_WINDOW", self.mainwindows)

        #初始化log信息
        setup_logging()

        self.ConfigData = Config_Data.Get_Data()
        # 创建主框架
        self.frame = tk.Frame(self.root, bd=2, relief=tk.GROOVE)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.CommOption_frame = ttk.LabelFrame(self.frame,text="选择通讯方式")
        self.CommOption_frame.place(x=0,y=5,width=700,height=260)
        self.Comm_option = tk.StringVar()
        self.Comm_option.set("USB")
        #串口
        self.serial_devices = Comm_class.List_SerialCom()
        self.SerialComm = tk.Radiobutton(self.CommOption_frame, text="串口", variable=self.Comm_option, value="串口")
        self.SerialComm.place(x=10,y=10)
        self.SerialNum_entry = ttk.Combobox(self.CommOption_frame, width=10,state='readonly')  # 根据实际情况修改串口号列表
        self.SerialNum_entry.place(x=80,y=10)
        self.SerialNum_entry['values'] = self.serial_devices
        if  self.serial_devices:
            self.SerialNum_entry.set(self.serial_devices[0])
        self.SerialNum_entry.bind("<Button-1>", self.refresh_serial_devices)

        self.Serial_baud_rate = tk.Label(self.CommOption_frame, text="波特率:")
        self.Serial_baud_rate.place(x=200,y=10)  
        self.Serialbaud_entry = ttk.Combobox(self.CommOption_frame, width=8, values=['2400', '4800', '9600', '19200', '38400', '57600',
                                                                                       '115200', '230400'])  # 根据实际情况修改串口号列表
        self.Serialbaud_entry.place(x=250,y=10)
        

        self.SerialCheck = tk.Label(self.CommOption_frame, text="校验:")
        self.SerialCheck.place(x=360,y=10)  

        self.SerialCheck_entry = ttk.Combobox(self.CommOption_frame, width=8, values=['NONE', 'ODD', 'EVEN'])  # 根据实际情况修改串口号列表
        self.SerialCheck_entry.place(x=400,y=10)
        self.SerialCheck_entry.set('NONE')
        #USB
        self.usb_devices = Comm_class.List_UsbCom()
        self.USBComm = tk.Radiobutton(self.CommOption_frame, text="USB", variable=self.Comm_option, value="USB")
        self.USBComm.place(x=10,y=40)
        self.USBNumber_entry = ttk.Combobox(self.CommOption_frame, width=80)
        self.USBNumber_entry['values'] = self.usb_devices
        if  self.usb_devices:
            self.USBNumber_entry.set(self.usb_devices[0])
        self.USBNumber_entry.place(x=80,y=40)
        self.USBNumber_entry.bind("<Button-1>", self.refresh_usb_devices)

        #网口
        self.EthernetComm = tk.Radiobutton(self.CommOption_frame, text="网口", variable=self.Comm_option, value="网口")
        self.EthernetComm.place(x=10,y=70)      
        self.EthernetIp = tk.Entry(self.CommOption_frame,width=18)
        self.EthernetIp.place(x=80,y=70)
        self.PortNum_label = tk.Label(self.CommOption_frame,text="端口号",font=("仿宋",12))
        self.PortNum_label.place(x=250,y=70)   
        self.PortNum_entry = tk.Entry(self.CommOption_frame,width=18)
        self.PortNum_entry.place(x=310,y=70)   
        #初始化网口地址
        if self.ConfigData != None and self.ConfigData["EthIp"]:
            self.EthernetIp.insert(0,self.ConfigData["EthIp"])
        if self.ConfigData != None and self.ConfigData["EthPort"]:
            self.PortNum_entry.insert(0,self.ConfigData["EthPort"])
        #并口
        self.LPTComm = tk.Radiobutton(self.CommOption_frame, text="LPT", variable=self.Comm_option, value="LPT")
        self.LPTComm.place(x=10,y=100)     
        self.LPTComm_entry = ttk.Combobox(self.CommOption_frame,width=18,values=['1'])
        self.LPTComm_entry.place(x=80,y=100) 

        #打开端口
        self.OpenPort_button = tk.Button(self.CommOption_frame, text="打开端口",width=28,command=self.OpenPort,font=("仿宋",12,"bold"))
        self.OpenPort_button.place(x=10,y=150)     
 
        #关闭端口
        self.ClosePort_button = tk.Button(self.CommOption_frame, text="关闭端口",width=28,command=self.ClosePort,font=("仿宋",12,"bold"))
        self.ClosePort_button.place(x=10,y=200)     
        self.ClosePort_button.config(state='disabled')

        #测试
        self.Test_button = tk.Button(self.CommOption_frame, text="测试",width=28,command=self.connect_test,font=("仿宋",12,"bold"))
        self.Test_button.place(x=400,y=150) 
        self.Test_button.config(state='disabled')

        #创建一个日志文本框
        self.log_frame = ttk.LabelFrame(self.frame,text="日志")
        self.log_frame.place(x=0,y=270,width=700,height=200)
        self.log_scrollbar = ttk.Scrollbar(self.log_frame)
        self.log_scrollbar.grid(row=0, column=1, padx=1, pady=1,sticky='ns')
        self.log_text = tk.Text(self.log_frame, height=12, width=75,yscrollcommand=self.log_scrollbar.set)
        self.log_text.grid(row=0, column=0, padx=1, pady=1)
        self.log_scrollbar.config(command=self.log_text.yview)

        #清空日志按钮
        Clear_log_button = tk.Button(self.log_frame, text="清空日志",width=8,command=self.Clear_log,font=("仿宋",12,"bold"))
        Clear_log_button.grid(row=0, column=2, padx=1, pady=1,sticky='n')
        #保存日志按钮
        Save_log_button = tk.Button(self.log_frame, text="保存日志",width=8,command=self.Save_log,font=("仿宋",12,"bold"))
        Save_log_button.grid(row=0, column=2, padx=1, pady=50,sticky='n')

    def refresh_usb_devices(self, event):
        self.USBNumber_entry['values'] = []  # 清空值
        self.USBNumber_entry.set('')
        self.usb_devices = Comm_class.List_UsbCom()    # 刷新USB设备列表
        self.USBNumber_entry['values'] = self.usb_devices  # 更新Combobox的值

    def refresh_serial_devices(self, event):
        self.serial_devices = Comm_class.List_SerialCom()    # 刷新USB设备列表
        self.SerialNum_entry['values'] = self.serial_devices  # 更新Combobox的值

    def OpenSerial_port(self):
        if not self.serial_devices:
            messagebox.showerror("错误", "打开端口失败：未检测到串口设备")
            log_message("打开端口失败：未检测到串口设备。",logging.ERROR)
         # 禁用所有控件
        else :
            baudrate = int(self.Serialbaud_entry.get())
            ret = Comm_class.Open_serialCom(self.SerialNum_entry.get(),baudrate)
            if not ret:
                messagebox.showerror("错误", "打开串口失败")
                return                
            for widget in self.CommOption_frame.winfo_children():
                widget.config(state='disabled')
            # 仅保留关闭端口按钮可用
            self.ClosePort_button.config(state='normal')
            self.Test_button.config(state='normal')  
            log_message("打开串口",logging.DEBUG)

    def OpenUsb_port(self):
        if not self.usb_devices:
            messagebox.showerror("错误", "打开端口失败：未检测到USB设备。")
            log_message("打开端口失败：未检测到USB设备",logging.ERROR)
         # 禁用所有控件
        else :
            ret = Comm_class.Open_UsbCom() 
            if not ret :
                messagebox.showerror("错误", "打开端口失败")
                log_message("打开USB端口失败",logging.ERROR)
                return 
            for widget in self.CommOption_frame.winfo_children():
                widget.config(state='disabled')
            # 仅保留关闭端口按钮可用
            self.ClosePort_button.config(state='normal')
            self.Test_button.config(state='normal')   
            log_message("打开USB端口",logging.DEBUG)
    def OpenEth_port(self):
        EthernetIp = self.EthernetIp.get()
        EthernetPort= int(self.PortNum_entry.get())
        ret = Comm_class.Open_EthernetTcp(EthernetIp,EthernetPort)
        if not ret:
            messagebox.showerror("错误", "网络连接失败")
            return                
        for widget in self.CommOption_frame.winfo_children():
            widget.config(state='disabled')
            # 仅保留关闭端口按钮可用
        self.ClosePort_button.config(state='normal')
        self.Test_button.config(state='normal')  
        log_message("网络连接成功",logging.DEBUG)

    def OpenLpt_port(self):
        pass

    def handle_default(self):
        pass

    def OpenPort(self):
        CommType = self.Comm_option.get()
        switcher = {
            '串口' : self.OpenSerial_port,
            'USB'  : self.OpenUsb_port,
            '网口' : self.OpenEth_port,
            'LPT'  : self.OpenLpt_port,
        }
        handler =  switcher.get(CommType, self.handle_default)
        handler()

    def ClosePort(self):
        # 启用所有控件
        for widget in self.CommOption_frame.winfo_children():
            widget.config(state='normal')
        # 测试按钮置灰
        self.Test_button.config(state='disabled')
        self.ClosePort_button.config(state='disabled')
        if  self.Comm_option.get() == "USB" :
            Comm_class.Close_UsbCom()
        elif self.Comm_option.get() == "串口":
            Comm_class.Close_serialCom()
        elif self.Comm_option.get() == "网口":
            Comm_class.Close_EthernetTcp()
            
    def connect_test(self):
        global Global_Comtype
        Global_Comtype = self.Comm_option.get()
        self.Open_mainUi()
        # 清空文本框的log
        self.log_text.delete(1.0, tk.END)


    def Open_mainUi(self):
        self.root.withdraw()
        main_ui = tk.Toplevel()
        MainUI(main_ui, self.root,self)

    #清空队列，但是不清空log文件
    def Clear_log(self):
        #清空文本框的log
        self.log_text.delete(1.0, tk.END)
        #清空log文件
        Clear_logfile()

    def Save_log(self):
        content = self.log_text.get(1.0, tk.END)
        # 弹出文件保存对话框
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                               filetypes=[("Text files", "*.txt"), 
                                                          ("All files", "*.*")])
        if file_path:  # 用户选择了文件路径
            with open(file_path, 'w') as file:
                file.write(content)  # 将内容写入文件
    def mainwindows(self):
        #保存网口信息
        ret = False
        if self.ConfigData :
            ret = Config_Data.Modify_Data("EthIp",value=self.EthernetIp.get())
            ret &= Config_Data.Modify_Data("EthPort",value=self.PortNum_entry.get())
            if ret:
                Config_Data.Save_Data()
        self.root.destroy()

class MainUI:
    def __init__(self, root,startup_window,startup_class):
        self.root = root
        self.startup_window = startup_window
        self.startup_class = startup_class
        self.root.title("测试部自研工具")
        self.root.geometry("700x500+600+300")

        #绑定关闭窗口
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # 创建Notebook部件，用于切换不同的选项卡
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # 添加"速度测试"选项卡
        self.speed_test = Speed_Test(self.notebook)
        self.notebook.add(self.speed_test.frame, text="速度测试")

        # 添加"打印效果测试"选项卡
        self.print_quality_test = Quality_Test(self.notebook)
        self.notebook.add(self.print_quality_test.frame, text="打印效果测试")

        #添加驱动测试的选项卡
        self.driver_test = Driver_Test(self.notebook)
        self.notebook.add(self.driver_test.frame, text="驱动测试")

        #添加Tspl测试的选项卡
        self.Tslp_test = Tspl_Test(self.notebook)
        self.notebook.add(self.Tslp_test.frame, text="TSPL指令测试")

        #添加ESC测试的选项卡
        self.Esc_test = Esc_Test(self.notebook)
        self.notebook.add(self.Esc_test.frame, text="ESC指令测")

        #添加网络测试的选项卡
        self.Net_test = Netword_Test(self.notebook)
        self.notebook.add(self.Net_test.frame,text="网络/蓝牙测试")


        #参数设置
        self.Paras_set = Paras_Set(self.notebook)
        self.notebook.add(self.Paras_set.frame,text="参数设置")

        #自定义参数设置
        self.Ram_test = RAM_Test(self.notebook)
        self.notebook.add(self.Ram_test.frame,text="自定义参数设置")

        #读写队列
        global Global_Comtype  # 引用全局变量
        Comtype = Global_Comtype
        self.read_thread  = queue_handler.start_read_thread(Comtype)
        #接收队列
        self.receive_thread  = queue_handler.start_receive_thread(Comtype,self.Esc_test.insert_recetext)

    def on_close(self):
        global Global_Comtype  # 引用全局变量
        self.root.destroy()
        self.startup_window.deiconify()
        queue_handler.stop_read_thread()
        self.read_thread.join()
        if Global_Comtype == "USB":
            self.receive_thread.join()
        Data = Rtn_logmessage()
        self.startup_class.log_text.insert(tk.END, Data + '\n')


if __name__ == "__main__":
    root = tk.Tk()
    app = StartUpWindow(root)
    root.mainloop()
