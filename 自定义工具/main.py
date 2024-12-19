
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
from APP.logger import logger_init, Rtn_logmessage,log_message, Clear_logfile
from APP.user_data import ConfigParas
from APP.globals import CONFIG



Global_Comtype = None

class StartUpWindow:
    def __init__(self, root):
        '''
            Args:
                self: 当前StartUpWindow 对象的实例
                root:  tk.Tk() UI窗口的根对象
        '''
        self.root = root
        self.root.title(CONFIG['setup_windows']['win_title'])
        self.root.geometry(CONFIG['setup_windows']['win_geometry'])
        self.root.protocol("WM_DELETE_WINDOW", self.mainwindows)

        '''
            初始化数据:
            1_logger_init :log 初始化
            2_configparas_instance 配置信息实例获取
        '''
        logger_init()                                       #初始化log对象
        self.configparas_instance = ConfigParas()           #创建配置类的实例

        '''
            main_frame: 根组件
            comm_option_frame: 通信区域组件
            comm_type : 选通信类型的组件
        '''
        self.main_frame = tk.Frame(self.root, bd=2, relief=tk.GROOVE)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.comm_option_frame = ttk.LabelFrame(self.main_frame,text=CONFIG['setup_windows']['comm_option_name'])
        self.set_frame_position(self.comm_option_frame,"place",*CONFIG['setup_windows']['comm_option_position'])
        self.comm_type = tk.StringVar()
        self.comm_type.set("USB")

        '''
            串口:
            1)serial_radiobutton: 串口选择按钮组件
            2)serial_port_combobox: 串口端口号列表组件
            3)serial_baud_rate_label: 波特率label组件
            4)serial_baud_rate_entry: 波特率entry组件
            5)serial_parity_label : 校验方式label组件
            6)serial_parity_entry : 校验方式的entry组件
        '''
        #1)
        self.serial_port_lists = Comm_class.list_serial_com()
        self.serial_radiobutton = tk.Radiobutton(self.comm_option_frame, text=CONFIG['setup_windows']['serial_radiobutton_name'], variable=self.comm_type, value="串口")
        self.set_frame_position(self.serial_radiobutton,"place",*CONFIG['setup_windows']['serial_radiobutton_position'])
        #2)
        self.serial_port_combobox = ttk.Combobox(self.comm_option_frame, width=10,state='readonly')
        self.set_frame_position(self.serial_port_combobox,"place",*CONFIG['setup_windows']['serial_port_combobox_position'])
        self.serial_port_combobox['values'] = self.serial_port_lists
        if  self.serial_port_lists:
            self.serial_port_combobox.set(self.serial_port_lists[0])
        self.serial_port_combobox.bind("<Button-1>", self.refresh_serial_port_lists)
        #3)
        self.serial_baud_rate_label = tk.Label(self.comm_option_frame, text=CONFIG['setup_windows']['baud_rate_name']) 
        self.set_frame_position(self.serial_baud_rate_label,"place",*CONFIG['setup_windows']['baud_rate_position'])
        #4)
        self.serial_baud_rate_entry = ttk.Combobox(self.comm_option_frame, width=8, values=CONFIG['setup_windows']['baud_rate_value'])
        self.set_frame_position(self.serial_baud_rate_entry,"place",*CONFIG['setup_windows']['baud_rate_entry_positiopn'])
        self.serial_baud_rate_entry.set(CONFIG['setup_windows']['baud_rate_default_value'])
        #5)
        self.serial_parity_label = tk.Label(self.comm_option_frame, text=CONFIG['setup_windows']['serial_parity_name'])
        self.set_frame_position(self.serial_parity_label,"place",*CONFIG['setup_windows']['serial_parity_name_positiopn'])  
        #6)
        self.serial_parity_entry = ttk.Combobox(self.comm_option_frame, width=8, values=CONFIG['setup_windows']['serial_parity_values'])  # 根据实际情况修改串口号列表
        self.set_frame_position(self.serial_parity_entry,"place",*CONFIG['setup_windows']['serial_parity_entry_positiopn']) 
        self.serial_parity_entry.set(CONFIG['setup_windows']['serial_parity_default_values'])

        '''
            USB:
            1)usb_radiobutton: USB选择按钮组件
            2)usb_device_combobox: usb设备列表组件
        '''
        #1)
        self.usb_device_list = Comm_class.list_usb_devices()
        self.usb_radiobutton = tk.Radiobutton(self.comm_option_frame, text=CONFIG['setup_windows']['usb_radiobutton_name'], variable=self.comm_type, value="USB")
        self.set_frame_position(self.usb_radiobutton,"place",*CONFIG['setup_windows']['usb_radiobutton_position'])
        #2)
        self.usb_device_combobox = ttk.Combobox(self.comm_option_frame, width=80)
        self.usb_device_combobox['values'] = self.usb_device_list
        if  self.usb_device_list:
            self.usb_device_combobox.set(self.usb_device_list[0])
        self.set_frame_position(self.usb_device_combobox,"place",*CONFIG['setup_windows']['usb_device_combobox_position'])
        self.usb_device_combobox.bind("<Button-1>", self.refresh_usb_devices)

        '''
            网口：
            variable:
                eth_ip_value:  存储到配置文件的Ip数据
                eth_port_value: 存储到配置文件的port数据
            1)eth_radiobutton: 以太网选择按钮组件
            2)eth_ip_entry: 以太网ip 列表entry组件
            3)eth_port_label: 以太网port名称的lable组件
            3)eth_port_entry: 以太网port 列表entry组件
        '''
        #1）
        self.eth_radiobutton = tk.Radiobutton(self.comm_option_frame, text=CONFIG['setup_windows']['eth_radiobutton_name'], variable=self.comm_type, value="网口")
        self.set_frame_position(self.eth_radiobutton,"place",*CONFIG['setup_windows']['eth_radiobutton_position'])    
        #2）
        self.eth_ip_entry = tk.Entry(self.comm_option_frame,width=18)
        self.set_frame_position(self.eth_ip_entry,"place",*CONFIG['setup_windows']['eth_ip_entry_position'])    
        #3)
        self.eth_port_label = tk.Label(self.comm_option_frame,text=CONFIG['setup_windows']['eth_port_name'],font=("仿宋",12))
        self.set_frame_position(self.eth_port_label,"place",*CONFIG['setup_windows']['eth_port_name_position'])     
        #4)
        self.eth_port_entry = tk.Entry(self.comm_option_frame,width=18)
        self.set_frame_position(self.eth_port_entry,"place",*CONFIG['setup_windows']['eth_port_entry_position'])    
        
        eth_ip_value = self.configparas_instance.get_config_item("EthIp")
        eth_port_value = self.configparas_instance.get_config_item("EthPort")
        if eth_ip_value and eth_port_value:
            self.eth_ip_entry.insert(0,eth_ip_value)
            self.eth_port_entry.insert(0,eth_port_value)
            
        '''
            并口: 暂时未实现并口
            1)lpt_radiobutton: 并口选择按钮组件
            2)lpt_device_entry: 并口设备列表entry组件
        '''
        #1）
        self.lpt_radiobutton = tk.Radiobutton(self.comm_option_frame, text=CONFIG['setup_windows']['lpt_radiobutton_name'], variable=self.comm_type, value="LPT")
        self.set_frame_position(self.lpt_radiobutton,"place",*CONFIG['setup_windows']['lpt_radiobutton_position'])  
        #2）
        self.lpt_device_entry = ttk.Combobox(self.comm_option_frame,width=18,values=['null'])
        self.set_frame_position(self.lpt_device_entry,"place",*CONFIG['setup_windows']['lpt_entry_position'])  

        '''
            按钮：
            self.open_comm_button：打开通信端口按钮；
            self.close_comm_button：关闭通信端口按钮；
            self.func_test_button： 功能测试按钮
        '''
        self.open_comm_button = self.creat_setupwindow_button(self.comm_option_frame,"打开端口",28,self.open_comm_port,("仿宋",12,"bold"),(10,150))   
        self.close_comm_button = self.creat_setupwindow_button(self.comm_option_frame,"关闭端口",28,self.close_comm_port,("仿宋",12,"bold"),(10,200),_state="disabled")
        self.func_test_button = self.creat_setupwindow_button(self.comm_option_frame,"功能测试",28,self.main_func_test,("仿宋",12,"bold"),(400,150),_state="disabled")

        '''
            main_frame: 根组件
            log_frame: 日志组件区域

            log_clear_button: 清空日志
            log_save_button: 保存日志

        '''
        #创建一个日志文本框
        self.log_frame = ttk.LabelFrame(self.main_frame,text="日志")
        self.log_frame.place(x=0,y=270,width=700,height=200)
        self.log_scrollbar = ttk.Scrollbar(self.log_frame)
        self.log_scrollbar.grid(row=0, column=1, padx=1, pady=1,sticky='ns')
        self.log_text = tk.Text(self.log_frame, height=12, width=75,yscrollcommand=self.log_scrollbar.set)
        self.log_text.grid(row=0, column=0, padx=1, pady=1)
        self.log_scrollbar.config(command=self.log_text.yview)

        self.log_clear_button = self.creat_setupwindow_button(self.log_frame,"清空日志",8,self.clear_log_message,("仿宋",12,"bold"),_position=(0,2,1,1,'n') ,_mode="grid")  
        self.log_save_button = self.creat_setupwindow_button(self.log_frame,"保存日志",8,self.save_log_message,("仿宋",12,"bold"),_position=(0,2,1,50,'n') ,_mode="grid")  


    def refresh_usb_devices(self, event):
        '''
            描述：刷新usb设备，点击(usb_device_combobox)组件后会重新刷新usb设备信息;
        '''
        self.usb_device_combobox['values'] = []  # 清空值
        self.usb_device_combobox.set('')
        self.usb_device_list = Comm_class.list_usb_devices()    # 刷新USB设备列表
        self.usb_device_combobox['values'] = self.usb_device_list  # 更新Combobox的值

    def refresh_serial_port_lists(self, event):
        '''
            描述：刷新串口设备号，点击（serial_port_combobox）组件会重新刷新串口设备信息；
        '''
        self.serial_port_lists = Comm_class.list_serial_com()    # 刷新USB设备列表
        self.serial_port_combobox['values'] = self.serial_port_lists  # 更新Combobox的值

    def open_serial_port(self):
        '''
            描述：打开串口端口号；
        '''
        if not self.serial_port_lists:
            messagebox.showerror(CONFIG['error_display']['error_name'], CONFIG['error_display']['serial_error_code']['no_device_detected'])
            log_message(CONFIG['error_log_message']['serial_error_code']['no_device_detected'],logging.ERROR)
        else :
            baudrate = int(self.serial_baud_rate_entry.get())
            ret = Comm_class.Open_serialCom(self.serial_port_combobox.get(),baudrate)
            if not ret:
                messagebox.showerror(CONFIG['error_display']['error_name'], CONFIG['error_display']['serial_error_code']['failed_to_open_port'])
                log_message(CONFIG['error_log_message']['serial_error_code']['failed_to_open_port'],logging.ERROR)
                return                
            for widget in self.comm_option_frame.winfo_children():
                widget.config(state='disabled')
            self.close_comm_button.config(state='normal')
            self.func_test_button.config(state='normal')  
            log_message(CONFIG['debug_log_message']['code_1'],logging.DEBUG)

    def open_usb_port(self):
        '''
            描述：打开usb端口
        '''
        if not self.usb_device_list:
            messagebox.showerror(CONFIG['error_display']['error_name'],CONFIG['error_display']['usb_error']['no_device_detected'])
            log_message(CONFIG['error_log_message']['usb_error']['no_device_detected'],logging.ERROR)
        else :
            ret = Comm_class.Open_UsbCom() 
            if not ret :
                messagebox.showerror(CONFIG['error_display']['error_name'], CONFIG['error_display']['usb_error']['failed_to_open_port'])
                log_message(CONFIG['error_log_message']['usb_error']['failed_to_open_port'],logging.ERROR)
                return 
            for widget in self.comm_option_frame.winfo_children():
                widget.config(state='disabled')
            # 仅保留关闭端口按钮可用
            self.close_comm_button.config(state='normal')
            self.func_test_button.config(state='normal')   
            log_message(CONFIG['debug_log_message']['code_2'],logging.DEBUG)

    def open_network_port(self):
        '''
            描述：打开网络端口
            变量:
                eth_ip : 要连接的网络ip
                eth_port: 要连接的端口号
        '''
        eth_ip = self.eth_ip_entry.get()
        eth_port= int(self.eth_port_entry.get())
        ret = Comm_class.Open_EthernetTcp(eth_ip,eth_port)
        if not ret:
            messagebox.showerror(CONFIG['error_display']['error_name'], CONFIG['error_display']['network_error']['connection_failed'])
            return                
        for widget in self.comm_option_frame.winfo_children():
            widget.config(state='disabled')
            # 仅保留关闭端口按钮可用
        self.close_comm_button.config(state='normal')
        self.func_test_button.config(state='normal')  
        log_message(CONFIG['debug_log_message']['code_3'],logging.DEBUG)

    def open_lpt_port(self):
        '''
            描述：打开并口，暂未实现
        '''
        pass

    def handle_default(self):
        '''
            描述：通信方式回调，暂不实现
        '''
        pass

    def open_comm_port(self):
        '''
            打开通信功能
        '''
        comm_type = self.comm_type.get()
        switcher = {
            '串口' : self.open_serial_port,
            'USB'  : self.open_usb_port,
            '网口' : self.open_network_port,
            'LPT'  : self.open_lpt_port,
        }
        handler =  switcher.get(comm_type, self.handle_default)
        handler()

    def close_comm_port(self):
        '''
            关闭通信功能
        '''
        for widget in self.comm_option_frame.winfo_children():
            widget.config(state='normal')
        self.func_test_button.config(state='disabled')
        self.close_comm_button.config(state='disabled')
        if  self.comm_type.get() == "USB" :
            Comm_class.Close_UsbCom()
        elif self.comm_type.get() == "串口":
            Comm_class.Close_serialCom()
        elif self.comm_type.get() == "网口":
            Comm_class.Close_EthernetTcp()
            
    def main_func_test(self):
        '''
            描述：主要功能测试
        '''
        global Global_Comtype
        Global_Comtype = self.comm_type.get()
        self.open_main_ui()
        self.log_text.delete(1.0, tk.END)


    def open_main_ui(self):
        '''
           描述： 打开主串口UI
           self.root.withdraw(): 隐藏启动窗口
        '''
        self.root.withdraw()
        main_ui = tk.Toplevel()
        MainUI(main_ui, self.root,self)

    def clear_log_message(self):
        '''
            清除log信息
        '''
        self.log_text.delete(1.0, tk.END)
        Clear_logfile()

    def save_log_message(self):
        '''
            保存log信息到指定目录
        '''
        log_data = self.log_text.get(1.0, tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                               filetypes=[("Text files", "*.txt"), 
                                                          ("All files", "*.*")])
        if file_path:  # 用户选择了文件路径
            with open(file_path, 'w') as file:
                file.write(log_data)  # 将内容写入文件

    def mainwindows(self):
        '''
            关闭启动窗口的时候，会调用该函数
            variable:
                config_data:  存储到配置文件的数据
            ret : 返回值
        '''

        config_data = self.configparas_instance.get_config_data()
        ret = False
        if config_data:
            ret = self.configparas_instance.Modify_Data("EthIp",value=self.eth_ip_entry.get())
            ret &= self.configparas_instance.Modify_Data("EthPort",value=self.eth_port_entry.get())
            if ret:
                self.configparas_instance.Save_Data()
        self.root.destroy()

    def set_frame_position(self,frame,mode="place",_x = 0,_y=0,_height=0,_width=0):
        '''
            描述：用来设置组件的位置
            frame:主框架
            mode: 位置设置的方式：place，pack，grid
            _x : x坐标
            _y ：y坐标
            _height：组件高度
            _width ： 组件宽度
        '''
        if mode == "place":
            if _height and _width:
                frame.place(x=_x,y=_y,height=_height,width=_width)
            else :
                frame.place(x=_x,y=_y)
        else :
            pass
    def creat_setupwindow_button(self,_frame,_name="按钮",_width=8,_command=None,_font=("仿宋",0),_position=(0,0,0,0,'n'),_mode="place",_state="normal"):
        '''
            描述：用来创建一个按钮
            _frame:主框架
            _name: 按钮的名称
            _width: 按钮的宽度
            _command：点击按钮后执行的命令函数
            _font: 字体
        '''
        button = tk.Button(_frame, text=_name,width=_width,command=_command,font=_font)
        if _mode == "place":
            button.place(x=_position[0],y=_position[1])
        elif _mode == "grid":
            button.grid(row=_position[0], column=_position[1], padx=_position[2], pady=_position[3],sticky=_position[4])
        button.config(state=_state)
        return button

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
