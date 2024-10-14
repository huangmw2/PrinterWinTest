#Paras Test
import tkinter as tk
from tkinter import ttk

class Paras_Set:
    def __init__(self,parent):
        self.frame =tk.Frame(parent,bd=2,relief=tk.GROOVE)
        self.frame.pack(fill=tk.BOTH,expand=True)
        if __name__ == "__main__":
            self.root = parent
            self.root.title("参数设置")
            self.root.geometry("700x500+600+300")    
        #基础设置
        self.Basic_frame = ttk.LabelFrame(self.frame, text="基础设置",width=680,height=180)
        self.Basic_frame.place(x=0,y=0)
        #Part 1
        self.Part1_frame = ttk.LabelFrame(self.Basic_frame, text="Part 1",width=250,height=150)
        self.Part1_frame.place(x=0,y=0)   
        self.Part1_frame.grid_propagate(False)  # 禁止根据内容自动调整大小
        self.baud_label = tk.Label(self.Part1_frame, text="波特率:",width=10)
        self.baud_label.grid(row=0, column=0, padx=1, pady=1, sticky="wn")

        self.baud_rate = ttk.Combobox(self.Part1_frame, values=["9600", "19200", "38400", "57600", "115200"], state="readonly",width=10)
        self.baud_rate.grid(row=0, column=1, padx=1, pady=1,sticky="wn")
        self.baud_rate.set("9600")  # 默认值

        self.flow_label = tk.Label(self.Part1_frame, text="流控:",width=10)
        self.flow_label.grid(row=1, column=0, padx=1, pady=1, sticky="wn")
        self.flow_control = ttk.Combobox(self.Part1_frame, values=["硬件流控", "软件流控"], state="readonly",width=10)
        self.flow_control.grid(row=1, column=1, padx=1, pady=1, sticky="wn")
        self.flow_control.set("硬件流控")  # 默认值

        self.languge_label = tk.Label(self.Part1_frame, text="设置语言:",width=10)
        self.languge_label.grid(row=2, column=0, padx=1, pady=1, sticky="w")
        self.languge_label = encoding = ttk.Combobox(self.Part1_frame, values=["UTF-8", "GBK", "ASCII"], state="readonly",width=10)
        self.languge_label = encoding.grid(row=2, column=1, padx=1, pady=1, sticky="w")
        self.languge_label = encoding.set("UTF-8")  # 默认值

       # set_button = tk.Button(self.Part1_frame, text="设置", width=10, command=lambda: print("基本参数设置已保存"))
      #  set_button.grid(row=2, column=2, padx=5, pady=5)    
            #Part 2

if __name__ == "__main__":
    root = tk.Tk()
    app = Paras_Set(root)
    root.mainloop()