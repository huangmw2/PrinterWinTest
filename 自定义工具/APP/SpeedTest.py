# speed_test.py
import tkinter as tk
from tkinter import ttk

class Speed_Test:
    def __init__(self, parent):   
        #创建一个矩形区域
        self.frame = tk.Frame(parent, bd=2, relief=tk.GROOVE)
        self.frame.pack(fill=tk.BOTH, expand=True)
		#发送文件
        self.label = tk.Label(self.frame, text="时间:00:00.0", font=("Helvetica", 32))
        self.label.pack(padx=20, pady=(20, 0))
        # 添加第二个Label控件
        self.label2 = tk.Label(self.frame, text="速度:000mm/s", font=("Helvetica", 32))
        self.label2.pack(padx=20, pady=(0, 10))  # 垂直方向的间距调整为20像素

  
        # 串口设置部分
        self.label_com_port = tk.Label(self.frame, text="选择串口号:")
        self.label_com_port.place(x=0,y=150)

        self.com_port_entry = ttk.Combobox(self.frame, width=10, values=['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9'])  # 根据实际情况修改串口号列表
        self.com_port_entry.place(x=80,y=150)
        self.com_port_entry.set('COM3')
        self.label_baud_rate = tk.Label(self.frame, text="输入波特率:")
        self.label_baud_rate.place(x=0,y=180)

        self.baud_rate_entry = tk.Entry(self.frame, width=10)
        self.baud_rate_entry.place(x=80,y=180)
        self.baud_rate_entry.insert(0, "115200")  # 默认波特率为115200
        #打印机数据选择
        self.label_speed = tk.Label(self.frame, text="打印速度设置：")
        self.label_speed.place(x=0,y=210)
        self.speep_entry = ttk.Combobox(self.frame, width=10, values=['1', '2', '3', '4', '5', '6', '7', '8'])  # 根据实际情况修改串口号列表
        self.speep_entry.place(x=80,y=210)
        self.speep_entry.set('8')
        self.speed_set_button = tk.Button(self.frame, text="设置", width=10, command=self.Print_speed_set)
        self.speed_set_button.place(x=180,y=210)  # 垂直方向上部分间距为20像素

        # 发送选项部分
        self.send_option = tk.StringVar()
        self.send_option.set("start_timer")

        self.radio_send_now = tk.Radiobutton(self.frame, text="发送马上计时", variable=self.send_option, value="start_timer")
        self.radio_send_now.place(x=200,y=150)
        self.radio_send_after = tk.Radiobutton(self.frame, text="发送完后开始计时", variable=self.send_option, value="start_after_send")
        self.radio_send_after.place(x=200,y=180)

        #2寸和3寸选择
        self.size_option = tk.StringVar()
        self.size_option.set("two_inches")
		
        self.radio_Two_Inches = tk.Radiobutton(self.frame, text="2寸", variable=self.size_option, value="two_inches")
        self.radio_Two_Inches.place(x=330,y=150)
        self.radio_Three_Inches = tk.Radiobutton(self.frame, text="3寸", variable=self.size_option, value="three_inches")
        self.radio_Three_Inches.place(x=330,y=180)
		
        # 开始和复位按钮
        self.start_stop_button = tk.Button(self.frame, text="开始", width=10, command=self.start_stop_timer)
        self.start_stop_button.place(x=0,y=250)  # 垂直方向上部分间距为20像素
		

        self.reset_button = tk.Button(self.frame, text="复位", width=10, command=self.reset_timer)
        self.reset_button.place(x=90,y=250)  # 垂直方向上部分间距为20像素

        # 强制结束按钮
        self.confirm_button = tk.Button(self.frame, text="保存", width=10, command=self.save_data)
        self.confirm_button.place(x=180,y=250) 
		#清空文件
        #self.clear_data()

    def Print_speed_set(self):
        print("test")

    def start_stop_timer(self):
        print("test")

    def reset_timer(self):
        print("test")
        
    def save_data(self):
        print("test")