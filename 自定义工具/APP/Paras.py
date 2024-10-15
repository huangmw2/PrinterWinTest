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
        #波特率
        self.baud_label = tk.Label(self.Basic_frame, text="波特率:")
        self.baud_label.place(x=0,y=5)

        self.baud_rate = ttk.Combobox(self.Basic_frame, values=["9600", "19200", "38400", "57600", "115200"], state="readonly",width=10)
        self.baud_rate.place(x=50,y=5)
        self.baud_rate.set("9600")  # 默认值

        set_button = tk.Button(self.Basic_frame, text="设置", width=8, command=self.SetParas(Num=0))
        set_button.place(x=150,y=0)   
        #流控
        self.flow_label = tk.Label(self.Basic_frame, text="流控:")
        self.flow_label.place(x=0,y=45)

        self.flow_control = ttk.Combobox(self.Basic_frame, values=["硬件流控", "软件流控"], state="readonly",width=10)
        self.flow_control.place(x=50,y=45)
        self.flow_control.set("硬件流控")  # 默认值
        set_flow_button = tk.Button(self.Basic_frame, text="设置", width=8, command=self.SetParas(Num=1))
        set_flow_button.place(x=150,y=40)   
        #流控
        self.languge_label = tk.Label(self.Basic_frame, text="语言:")
        self.languge_label.place(x=0,y=85)

        self.languge_label = encoding = ttk.Combobox(self.Basic_frame, values=["UTF-8", "GBK", "ASCII"], state="readonly",width=10)
        self.languge_label = encoding.place(x=50,y=85)
        self.languge_label = encoding.set("UTF-8")  # 默认值
        set_languge_button = tk.Button(self.Basic_frame, text="设置", width=8, command=self.SetParas(Num=2))
        set_languge_button.place(x=150,y=80) 

        #part 2

        self.Part_frame = ttk.LabelFrame(self.frame, text="Part 2")
        self.Part_frame.place(x=250,y=0,width=200,height=180)

        self.font_label = tk.Label(self.Part_frame, text="字体设置:")
        self.font_label.place(x=0,y=1)
        font_size = ttk.Combobox(self.Part_frame, values=["12x24", "8x16", "16x32"], state="readonly",width=8)
        font_size.place(x=70,y=1)
        font_size.set("12x24")  # 默认值

        self.density_label = tk.Label(self.Part_frame, text="打印浓度:")
        self.density_label.place(x=0,y=30)
        print_density = ttk.Combobox(self.Part_frame, values=["淡淡", "微淡", "正常", "加深"], state="readonly",width=8)
        print_density.place(x=70,y=30)
        print_density.set("微淡")  # 默认值

        self.feed_label = tk.Label(self.Part_frame, text="进纸:")
        self.feed_label.place(x=0,y=60)
        paper_feed = ttk.Combobox(self.Part_frame, values=["0x0A", "0x0D"], state="readonly",width=8)
        paper_feed.place(x=70,y=60)
        paper_feed.set("0x0A")  # 默认值

        # 切刀类型和蜂鸣器
        self.cutter_label = tk.Label(self.Part_frame, text="切刀类型:")
        self.cutter_label.place(x=0,y=90)
        cutter_type = ttk.Combobox(self.Part_frame, values=["不切", "切纸"], state="readonly",width=8)
        cutter_type.place(x=70,y=90)
        cutter_type.set("不切")  # 默认值

        self.buzzer_var = tk.IntVar()
        self.buzzerSwitch =tk.Checkbutton(self.Part_frame, text="蜂鸣器", variable=self.buzzer_var)
        self.buzzerSwitch.place(x=0,y=120)

        self.knife_var = tk.IntVar()
        self.knifeSwitch =tk.Checkbutton(self.Part_frame, text="切刀", variable=self.knife_var)
        self.knifeSwitch.place(x=70,y=120)

        self.partset_button = tk.Button(self.Part_frame, text="设置", width=8, command=self.SetParas(Num=3))
        self.partset_button.place(x=125,y=120) 
       # set_button = tk.Button(self.Part1_frame, text="设置", width=10, command=lambda: print("基本参数设置已保存"))
      #  set_button.grid(row=2, column=2, padx=5, pady=5)    
            #Part 2
    def SetParas(self,Num):
        pass
if __name__ == "__main__":
    root = tk.Tk()
    app = Paras_Set(root)
    root.mainloop()