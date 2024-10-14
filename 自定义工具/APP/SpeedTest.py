# speed_test.py
import tkinter as tk
from tkinter import ttk, messagebox
import time
import struct
import os
import logging

try:
    from APP.Usbcom import Comm_class  # 绝对导入
except ImportError:
    from Usbcom import Comm_class  # 相对导入

if __name__ == "__main__":
    from Queue import queue_handler
    from Log import log_message  
else :
    from APP.Queue import queue_handler
    from APP.Log import log_message 

class Speed_Test:
    def __init__(self, parent):   
        self.is_running = False
        self.start_time = 0  # 保存计时开始的时间
        self.elapsed_time = 0  # 保存已经过去的时间
        self.timer_id = None  # 保存 after() 的定时器 ID
        self.Print_speed = 0
        # 创建存储速度数据的列表
        self.AveSpeed_data = []

        self.threeinches_path = os.getcwd() + r"\Data\Speed\threeinches.hex"
        self.twoinches_path =  os.getcwd() + r"\Data\Speed\twoinches.hex"
        
        if __name__ == "__main__":
            self.root = parent
            self.root.title("Speed测试")
            self.root.geometry("700x500+600+300")        
        #创建一个矩形区域
        self.frame = tk.Frame(parent, bd=2, relief=tk.GROOVE)
        self.frame.pack(fill=tk.BOTH, expand=True)
		#发送文件
        self.label = tk.Label(self.frame, text="时间:00:00.0", font=("Helvetica", 32))
        self.label.pack(padx=20, pady=(20, 0))
        # 添加第二个Label控件
        self.label2 = tk.Label(self.frame, text="速度:000mm/s", font=("Helvetica", 32))
        self.label2.pack(padx=20, pady=(0, 10))  # 垂直方向的间距调整为20像素
        # 发送选项部分
        self.label_Timertype = tk.Label(self.frame, text="计时方式：",font=("仿宋",12,"bold"))
        self.label_Timertype.place(x=10,y=150)       
        self.send_option = tk.StringVar()
        self.send_option.set("start_timer")
        self.radio_send_now = tk.Radiobutton(self.frame, text="发送马上计时", variable=self.send_option, value="start_timer",font=("仿宋",12))
        self.radio_send_now.place(x=90,y=150)
        self.radio_send_after = tk.Radiobutton(self.frame, text="发送完后开始计时", variable=self.send_option, value="start_after_send",font=("仿宋",12))
        self.radio_send_after.place(x=220,y=150)
        #2寸和3寸选择
        self.label_Paperinches = tk.Label(self.frame, text="纸张尺寸：",font=("仿宋",12,"bold"))
        self.label_Paperinches.place(x=10,y=180)  
        self.size_option = tk.StringVar()
        self.size_option.set("two_inches")
        self.radio_Two_Inches = tk.Radiobutton(self.frame, text="2寸", variable=self.size_option, value="two_inches",font=("仿宋",12),command=self.update_paper_length)
        self.radio_Two_Inches.place(x=90,y=180)
        self.radio_Three_Inches = tk.Radiobutton(self.frame, text="3寸", variable=self.size_option, value="three_inches",font=("仿宋",12),command=self.update_paper_length)
        self.radio_Three_Inches.place(x=220,y=180)
        #纸张的长度
        self.label_Paperlength  = tk.Label(self.frame, text="纸张长度：",font=("仿宋",12,"bold"))
        self.label_Paperlength.place(x=10,y=210)   
        self.Paperlength_entry = tk.Entry(self.frame,width=10)
        self.Paperlength_entry.place(x=100,y=210) 
        if self.size_option.get() == "two_inches":
            self.Paperlength_entry.insert(0,"1280") 
        else :
            self.Paperlength_entry.insert(0,"1600") 
          
        self.label_mmunit = tk.Label(self.frame, text="MM",font=("仿宋",12))
        self.label_mmunit.place(x=180,y=210)     
        self.LengthSet_button = tk.Button(self.frame, text="长度设置", width=10, command=self.SetPaperLength,font=("仿宋",12))
        self.LengthSet_button.place(x=210,y=210)  
        #打印机数据选择
        self.label_speed = tk.Label(self.frame, text="打印速度：",font=("仿宋",12,"bold"))
        self.label_speed.place(x=10,y=240)
        self.speep_entry = ttk.Combobox(self.frame, width=10, values=['1', '2', '3', '4', '5', '6', '7', '8'])  # 根据实际情况修改串口号列表
        self.speep_entry.place(x=100,y=240)
        self.speep_entry.set('8')
        self.speed_set_button = tk.Button(self.frame, text="速度设置", width=10, command=self.Print_speed_set,font=("仿宋",12))
        self.speed_set_button.place(x=210,y=240)  # 垂直方向上部分间距为20像素

        #平均速度
        self.label_AveSpeed = tk.Label(self.frame, text="平均速度：",font=("仿宋",12,"bold"))
        self.label_AveSpeed.place(x=10,y=270)
        self.AveSpeed_entry = tk.Entry(self.frame,width=10)
        self.AveSpeed_entry.place(x=100,y=270)
        # 禁止键盘输入的绑定
        self.AveSpeed_entry.bind("<Key>", lambda e: "break")
        self.AveSpeed_entry.config(state='disabled')

        # 开始和复位按钮
        self.start_stop_button = tk.Button(self.frame, text="开始", width=10, command=self.start_stop_timer,font=("仿宋",12),bg="green")
        self.start_stop_button.place(x=0,y=310)  
		
        self.reset_button = tk.Button(self.frame, text="复位", width=10, command=self.reset_timer,font=("仿宋",12))
        self.reset_button.place(x=120,y=310)  

        # 平均速度按钮
        self.AverageSpeed_button = tk.Button(self.frame, text="平均速度", width=10, command=self.average_speed,font=("仿宋",12))
        self.AverageSpeed_button.place(x=240,y=310) 

		#清除数据按钮
        self.ClearSpeedData_button = tk.Button(self.frame, text="清除数速度数据", width=14, command=self.ClearAveData,font=("仿宋",12))
        self.ClearSpeedData_button.place(x=360,y=310)

    def Print_speed_set(self):
        start_flag = b'\x02\x00'
        command = struct.pack('<H', 0x92)  # 小端格式的命令
        param_h = b'\x00\x00'
        param_l = b'\x00\x00'
        device_id = b'\x00\x00\x00\x00'  # 设备ID
        data_length = 2
        data_length_bytes = struct.pack('<H', data_length)  # 小端格式的数据长度
        # 计算校验和
        checksum = start_flag[0] ^ start_flag[1] ^ command[0] ^ command[1]
        checksum ^= param_h[0] ^ param_h[1] ^ param_l[0] ^ param_l[1]
        checksum ^= device_id[0] ^ device_id[1] ^ device_id[2] ^ device_id[3]
        checksum ^= data_length_bytes[0] ^ data_length_bytes[1]
        #命令
        speed = self.speep_entry.get()
        com_data = b'\x83' + struct.pack('B', int(speed))
        # 对数据部分进行异或计算
        com_data_checksum = 0
        for byte in com_data:
            com_data_checksum ^= byte   
        # 创建包
        packet = start_flag + command + param_h + param_l + device_id + data_length_bytes + bytes([checksum]) + b'\x00' + com_data + bytes([com_data_checksum]) 
        log = "设置打印速度为：" + speed      
        queue_handler.write_to_queue(packet,log) 
        #设置参数，后续可能需要显示设置成功或者失败

    def start_stop_timer(self):
        if not os.path.exists(self.twoinches_path):
            log = "没有找到2寸速度测试数据的路径:{}".format(self.twoinches_path)
            log_message(log,logging.ERROR)
            return 
        if not os.path.exists(self.threeinches_path):
            log = "没有找到3寸速度测试数据的路径:{}".format(self.threeinches_path)
            log_message(log,logging.ERROR)
            return 
        
        if not self.is_running:
            inches = self.size_option.get()
            SendType = self.send_option.get()
            Comtype = queue_handler.Get_ComType()
            if inches == "two_inches":
                try:
                    with open(self.twoinches_path, 'r') as file:
                        content = file.read()
                except Exception as e:
                    messagebox.showerror("错误", "打开2寸文件错误")
                log = "2寸速度测试"
            elif inches == "three_inches":
                try:
                    with open(self.threeinches_path, 'r') as file:
                        content = file.read()
                except Exception as e:
                    messagebox.showerror("错误", "打开3寸文件错误")
                log = "3寸速度测试"
            else :
                pass
            if not content:
                messagebox.showerror("错误", "速测测试数据为空")
                return 
            byte_data = bytes.fromhex(content)
            log_message(log,logging.DEBUG)
            for widget in self.frame.winfo_children():
                widget.config(state='disabled')
            # 仅保留停止按钮可用
            self.start_stop_button.config(state='normal')
            if SendType == "start_after_send":
                Comm_class.Print_SpeedData(byte_data,Comtype)
            # 开始计时
            self.is_running = True
            self.start_stop_button.config(text="停止", bg="red")
            self.start_time = time.time() - self.elapsed_time  # 记录开始时间，考虑已经过去的时间
            self.update_timer()  # 启动计时器
            self.start_stop_button.config(text="停止", bg="red")
            if SendType == "start_timer":
                Comm_class.Print_SpeedData(byte_data,Comtype)
    
        else:
            # 停止计时
            self.is_running = False
            if self.timer_id:
                self.frame.after_cancel(self.timer_id)  # 取消计时
            self.start_stop_button.config(text="开始", bg="green")
            Paperlength = int(self.Paperlength_entry.get())
            PrintTime = int(self.elapsed_time*10)
            self.Print_speed = Paperlength*10/PrintTime
            speed_format = f"速度:{int(self.Print_speed):03d}mm/s"
            self.label2.config(text=speed_format)
            # 在这里添加停止计时功能代码
            for widget in self.frame.winfo_children():
                widget.config(state='normal')
            self.AveSpeed_entry.config(state='disabled')
            if self.Print_speed :
                self.AveSpeed_data.append(self.Print_speed)

    def update_timer(self):
        # 计算已经过去的时间
        self.elapsed_time = time.time() - self.start_time
        minutes, seconds = divmod(self.elapsed_time, 60)
        milliseconds = int((self.elapsed_time - int(self.elapsed_time)) * 10) #取出第一位小数
        time_format = f"时间:{int(minutes):02}:{int(seconds):02}.{milliseconds}"
        self.label.config(text=time_format)
        # 如果计时器在运行，继续更新
        if self.is_running:
            self.timer_id = self.frame.after(100, self.update_timer)  # 每 100 毫秒更新一次

    def reset_timer(self):
        self.is_running = False
        self.elapsed_time = 0
        self.label.config(text="时间:00:00.0")
        self.label2.config(text="速度:000mm/s")
        self.start_stop_button.config(text="开始", bg="green")
        if self.timer_id:
            self.frame.after_cancel(self.timer_id)
        
    def average_speed(self):
        if self.AveSpeed_data:
            # 计算平均速度
            avg_speed = sum(self.AveSpeed_data) / len(self.AveSpeed_data)
            speed_format = f"{int(avg_speed):03d}mm/s"
            self.AveSpeed_entry.delete(0, tk.END)
            self.AveSpeed_entry.insert(speed_format)
    def ClearAveData(self):
        self.AveSpeed_data = []
        self.AveSpeed_entry.delete(0, tk.END) #请假控件列表

    def SetPaperLength(self):
        Paperlength = int(self.Paperlength_entry.get())
        PrintTime = int(self.elapsed_time*10)
        self.Print_speed = Paperlength*10/PrintTime
        speed_format = f"速度:{int(self.Print_speed):03d}mm/s"
        self.label2.config(text=speed_format)

    def update_paper_length(self):
        inches = self.size_option.get()
        if inches == "two_inches":
            self.Paperlength_entry.delete(0, tk.END)
            self.Paperlength_entry.insert(0,"1280")
        elif inches == "three_inches":
            self.Paperlength_entry.delete(0, tk.END)
            self.Paperlength_entry.insert(0,"1600")
        else :
            print("纸张长度选择错误")
        pass
if __name__ == "__main__":

    root = tk.Tk()
    app = Speed_Test(root)
    root.mainloop()