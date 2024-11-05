#TSPL Test
import os
import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
if __name__ == "__main__":
    from Queue import queue_handler
else :
    from APP.Queue import queue_handler

class Tspl_Test:
    def __init__(self,parent):
        #索引号
        self.index = 0
        #停止标志
        self.stop_flag = False
        #变量：是否循环发送
        self.loop_var = tk.BooleanVar()
        self.loop_var.set(False)
        #变量：数据的路径
        self.DataPath = os.getcwd() + r"\Data\TSPL\Tspl_config.txt"
        #列表：文本框的个数
        self.textboxs = []
        #列表：文本数的数据
        self.text_data_list = []
        #初始化文本框的数据，并保存到列表
        self.Load_TextData(self.DataPath)

        #创建主框架
        self.frame = tk.Frame(parent, bd=2, relief=tk.GROOVE)
        self.frame.pack(fill=tk.BOTH, expand=True)
        #创建按钮区域
        self.button_frame = tk.Frame(self.frame)
        self.button_frame.pack(side=tk.TOP, fill=tk.X)
        #创建一键测试按钮
        self.OneClick_test =  tk.Button(self.button_frame, text="一键测试",width=8,command=self.OneClickTest,font=("仿宋",12,"bold"))
        self.OneClick_test.pack(side=tk.LEFT, padx=2, pady=(1,0))
        #创建一个单条测试的按钮
        self.Delay_time = tk.Button(self.button_frame, text="单条测试",width=8,command=self.DelaySet,font=("仿宋",12,"bold"))
        self.Delay_time.pack(side=tk.LEFT, padx=2, pady=1)
        #创建测试条目的输入区
        self.TestNumber_entry = tk.Entry(self.button_frame,width=5)
        self.TestNumber_entry.pack(side=tk.LEFT, padx=1, pady=1)
        self.TestNumber_entry.insert(0,"1")       
        #时间间隔
        self.lable = tk.Label(self.button_frame,text="间隔:",font=("仿宋",10))
        self.lable.pack(side=tk.LEFT,padx=2,pady=10)
        #创建一个输入时间输入区域
        self.Delay_time_entry = tk.Entry(self.button_frame,width=7)
        self.Delay_time_entry.pack(side=tk.LEFT, padx=2, pady=1)
        self.Delay_time_entry.insert(0,"3000")
        #毫秒
        self.lable = tk.Label(self.button_frame,text="ms",font=("仿宋",10))
        self.lable.pack(side=tk.LEFT,padx=2,pady=10)    

        # 创建停止按钮
        self.Stop_button = tk.Button(self.button_frame,
                                     text="停止",
                                     width=5,
                                     command=self.StopAction,
                                     font=("仿宋", 10, "bold"))
        self.Stop_button.pack(side=tk.LEFT, padx=2, pady=1)  
        self.Stop_button.config(state='disabled')      
        #修改标签的宽度和高度
        self.control_frame = tk.Frame(self.frame)
        self.control_frame.pack(side=tk.TOP, fill=tk.X, pady=1)
        self.lable_Width = tk.Label(self.control_frame,text="标签宽度:",font=("仿宋",10))
        self.lable_Width.pack(side=tk.LEFT, padx=5, pady=1)
        #创建一个输入区域
        self.lable_Width_entry = tk.Entry(self.control_frame,width=5)
        self.lable_Width_entry.pack(side=tk.LEFT, padx=2, pady=1)
        self.lable_Width_entry.insert(0,"50")
        #修改高度
        self.lable_High = tk.Label(self.control_frame,text="标签高度:",font=("仿宋",10))
        self.lable_High.pack(side=tk.LEFT, padx=5, pady=1)
        #创建一个输入区域
        self.lable_High_entry = tk.Entry(self.control_frame,width=5)
        self.lable_High_entry.pack(side=tk.LEFT, padx=2, pady=1)
        self.lable_High_entry.insert(0,"40")
        #创建一个设置按钮
        self.SetParms_button = tk.Button(self.control_frame,text="设置",width=6,command=self.ParmsSet,font=("仿宋",10))
        self.SetParms_button.pack(side=tk.LEFT,padx=5, pady=1)
        #添加TSPL命令
        self.AddTsplCmd_button = tk.Button(self.control_frame,text="添加TSPL指令",width=12,command=self.AddCmd,font=("仿宋",10))
        self.AddTsplCmd_button.pack(side=tk.LEFT,padx=5, pady=1)
        #保存
        self.Save_Data_button = tk.Button(self.control_frame,text="保存数据",width=8,command=self.SaveData,font=("仿宋",10))
        self.Save_Data_button.pack(side=tk.LEFT,padx=2,pady=1)
        #创建画布和滚动条
        canvas = tk.Canvas(self.frame)
        scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas)


        # 将滚动区域放到画布上
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        # 确保滚动区域可以显示到画布中
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # 创建并显示文本框
        for i, data in enumerate(self.text_data_list):
            text_box = tk.Text(self.scrollable_frame, height=8, width=70,undo=True)
            text_box.pack(padx=10, pady=5, fill=tk.X)
            text_box.insert(tk.END, data)
            self.textboxs.append(text_box)

    def is_valid_data(self,s):
        """
        检查字符串是否只包含合法字符：'0~9', 'A~F', 空格和回车符。
        """
        # 正则表达式检查：允许0-9, A-F (不区分大小写), 空格和回车符
        return bool(re.match(r'^[0-9A-Fa-f \r\n]+$', s))
    
    def loop_Send(self):
        Delay_time = int(self.Delay_time_entry.get())
        if self.index >= len(self.textboxs):
            self.StopAction()

        if self.stop_flag == False:
            Data = self.textboxs[self.index].get("1.0", tk.END) 
            if self.is_valid_data(Data):
                print(Data)
            log = "发送第{}条,TSPL数据".format(self.index+1)
            queue_handler.write_to_queue(Data,log)
            self.index += 1 
            self.frame.after(Delay_time, self.loop_Send)
        else :
            print("通信结束") 

    def OneClickTest(self):
        for widget in self.button_frame.winfo_children():
            widget.config(state='disabled')
        for widget in self.control_frame.winfo_children():
            widget.config(state='disabled')
        self.Stop_button.config(state='normal',bg='red')
        self.index = 0
        self.stop_flag = False
        self.loop_Send()
        

    def DelaySet(self):
        Number = int(self.TestNumber_entry.get())
        if Number > len(self.textboxs) or Number == 0:
            messagebox.showerror("错误","输入的测试条目不对")
            return 
        Data = self.textboxs[Number-1].get("1.0", tk.END) 
        log = "发送第{}条,TSPL数据".format(Number)
        queue_handler.write_to_queue(Data,log)  

    def SaveData(self):
        """将文本数据保存到文件中，每个数据块用分隔符分隔。"""
        try:
            os.makedirs(os.path.dirname(self.DataPath), exist_ok=True)
            with open(self.DataPath, 'w', encoding='cp936',errors='replace') as file:
                for text_box in self.textboxs:
                    text_data = text_box.get("1.0", tk.END).strip()
                    file.write(text_data + '\n=====\n')
            messagebox.showinfo("保存成功","数据已成功保存到文件中。")
        except Exception as e:
            messagebox.showerror("保存失败", f"保存数据时发生错误: {e}")

    def Load_TextData(self,file_path):
        if not os.path.exists(file_path):
            return 
        with open(file_path, 'r', encoding='cp936',errors='replace') as file:
            content = file.read()
            self.text_data_list = content.split('=====')
            # 清除可能的空字符串
            self.text_data_list = [data.strip() for data in self.text_data_list if data.strip()]    

    def StopAction(self):
        print("停止按钮被点击")
        for widget in self.button_frame.winfo_children():
            widget.config(state='normal')
        for widget in self.control_frame.winfo_children():
            widget.config(state='normal')
        self.Stop_button.config(state='disabled',bg='white')
        self.stop_flag = True

    # 替换包含 "SIZE" 的行
    def replace_size_lines(self,text):
        width = self.lable_Width_entry.get()
        high = self.lable_High_entry.get()
        return re.sub(r"^SIZE.*$", f"SIZE {width} mm, {high} mm", text, flags=re.MULTILINE)
    
    def ParmsSet(self):
        # 更新原列表中的每个文本块
        for i in range(len(self.text_data_list)):
            self.text_data_list[i] = self.replace_size_lines(self.text_data_list[i])
        for i, data in enumerate(self.text_data_list):
            self.textboxs[i].delete("1.0", tk.END)
            self.textboxs[i].insert(tk.END, data)  # 设置文本框的数据
    def AddCmd(self):
        text_box = tk.Text(self.scrollable_frame, height=8, width=70,undo=True)
        text_box.pack(padx=10, pady=5, fill=tk.X)
        text_box.insert(tk.END, "")
        self.textboxs.append(text_box)

if __name__ == "__main__":

    root = tk.Tk()
    app = Tspl_Test(root)
    root.mainloop()