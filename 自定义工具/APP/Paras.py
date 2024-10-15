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

        self.baud_rate_value = ["9600", "19200", "38400", "57600", "115200","230400"]
        self.flow_control_value = ["硬件流控", "软件流控"]
        self.language_entry_value = [
            "CP932 SHIFT JIS", "UNICODE UCS-2", "CP950:BIG5", "CP936:GBK",
            "CP437:USA/Standard Europe", "Katakana", "CP850:Latin1;Western European",
            "CP860:Portuguese", "CP863:French Canadian", "CP865:Nordic", 
            "CP1251:Cyrillic", "CP866:Russian;Cyrillic", "CP1025:Cyrillic/Bulgarian",
            "CP773:Estonian/Lithuanian/Latvian", "Iran", "Reversed", "CP862:Hebrew",
            "CP1252:Latin1", "CP1253:Greek", "CP852:Latin2", "CP858:Latin1+Euro", 
            "Iran II", "CP1117:Latvian", "CP864:Arabic", "ISO-8859-1:West Europe", 
            "CP737:Greek", "CP1257:Baltic", "Thai", "CP720:Arabic", "CP855:Cyrillic", 
            "CP857:Turkish", "CP1250:Central Europe", "CP775:Estonian/Lithuanian/Latvian", 
            "CP1254:Turkish", "CP1255:Hebrew", "CP1256:Arabic", "CP1258:Vietnam", 
            "ISO-8859-2:Latin2", "ISO-8859-3:Latin3", "ISO-8859-6:Arabic", "ISO-8859-7:Greek", 
            "ISO-8859-8:Hebrew", "ISO-8859-9:Turkish", "ISO-8859-15:Latin3", "Thai2", 
            "CP856:Hebrew", "CP874:Thai", "EUC-KR", "UTF-8"
        ]
        self.font_size_value = ["9x17","12x24", "9x24", "16x18"]
        self.print_density_value = ["微淡", "正常", "微浓", "高浓"]
        self.paper_feed_value = ["0x0A", "0x0D"]
        self.cutter_type_value = ["不切", "最后一张切","指令切","单张切"]
        #基础设置
        self.Basic_frame = ttk.LabelFrame(self.frame, text="基础设置",width=680,height=180)
        self.Basic_frame.place(x=0,y=0) 
        #波特率
        self.baud_label = tk.Label(self.Basic_frame, text="波特率:")
        self.baud_label.place(x=0,y=5)

        self.baud_rate = ttk.Combobox(self.Basic_frame, values=self.baud_rate_value, state="readonly",width=10)
        self.baud_rate.place(x=50,y=5)
        self.baud_rate.set("9600")  # 默认值

        set_button = tk.Button(self.Basic_frame, text="设置", width=8, command=lambda:self.SetParas(0))
        set_button.place(x=150,y=0)   
        #流控
        self.flow_label = tk.Label(self.Basic_frame, text="流控:")
        self.flow_label.place(x=0,y=45)

        self.flow_control = ttk.Combobox(self.Basic_frame, values=self.flow_control_value, state="readonly",width=10)
        self.flow_control.place(x=50,y=45)
        self.flow_control.set("硬件流控")  # 默认值
        set_flow_button = tk.Button(self.Basic_frame, text="设置", width=8, command=lambda:self.SetParas(1))
        set_flow_button.place(x=150,y=40)   
        #流控
        self.languge_label = tk.Label(self.Basic_frame, text="语言:")
        self.languge_label.place(x=0,y=85)

        self.languge_entry = encoding = ttk.Combobox(self.Basic_frame, values=self.language_entry_value, state="readonly",width=20)
        self.languge_entry = encoding.place(x=50,y=85)
        self.languge_entry = encoding.set("UTF-8")  # 默认值
        self.set_languge_button = tk.Button(self.Basic_frame, text="设置", width=8, command=lambda:self.SetParas(2))
        self.set_languge_button.place(x=150,y=110) 

        #part 2

        self.Part_frame = ttk.LabelFrame(self.frame, text="Part 2")
        self.Part_frame.place(x=230,y=0,width=200,height=180)

        self.font_label = tk.Label(self.Part_frame, text="字体设置:")
        self.font_label.place(x=0,y=1)
        self.font_size = ttk.Combobox(self.Part_frame, values=self.font_size_value, state="readonly",width=8)
        self.font_size.place(x=70,y=1)
        self.font_size.set("12x24")  # 默认值

        self.density_label = tk.Label(self.Part_frame, text="打印浓度:")
        self.density_label.place(x=0,y=30)
        self.print_density = ttk.Combobox(self.Part_frame, values=self.print_density_value, state="readonly",width=8)
        self.print_density.place(x=70,y=30)
        self.print_density.set("正常")  # 默认值

        self.feed_label = tk.Label(self.Part_frame, text="进纸:")
        self.feed_label.place(x=0,y=60)
        self.paper_feed = ttk.Combobox(self.Part_frame, values=self.paper_feed_value, state="readonly",width=8)
        self.paper_feed.place(x=70,y=60)
        self.paper_feed.set("0x0A")  # 默认值

        # 切刀类型和蜂鸣器
        self.cutter_label = tk.Label(self.Part_frame, text="切刀类型:")
        self.cutter_label.place(x=0,y=90)
        self.cutter_type = ttk.Combobox(self.Part_frame, values=self.cutter_type_value, state="readonly",width=8)
        self.cutter_type.place(x=70,y=90)
        self.cutter_type.set("不切")  # 默认值

        self.buzzer_var = tk.IntVar()
        self.buzzerSwitch =tk.Checkbutton(self.Part_frame, text="蜂鸣器", variable=self.buzzer_var)
        self.buzzerSwitch.place(x=0,y=120)

        self.knife_var = tk.IntVar()
        self.knifeSwitch =tk.Checkbutton(self.Part_frame, text="切刀", variable=self.knife_var)
        self.knifeSwitch.place(x=70,y=120)

        self.partset_button = tk.Button(self.Part_frame, text="设置", width=8, command=lambda:self.SetParas(3))
        self.partset_button.place(x=125,y=120) 

        #Part 3
        self.Part2_frame = ttk.LabelFrame(self.frame, text="Part 3")
        self.Part2_frame.place(x=430,y=0,width=250,height=80)    

        self.sleep_label = tk.Label(self.Part2_frame, text="休眠时间:")
        self.sleep_label.place(x=0,y=1)
        self.sleep_entry = tk.Entry(self.Part2_frame, width=8)
        self.sleep_entry.place(x=70,y=1)
        self.sleep_entry.insert(0,"600")  # 默认值
        self.sleeps_label = tk.Label(self.Part2_frame, text="秒")
        self.sleeps_label.place(x=140,y=1)

        self.shutdown_label = tk.Label(self.Part2_frame, text="关机时间:")
        self.shutdown_label.place(x=0,y=30)
        self.shutdown_entry = tk.Entry(self.Part2_frame, width=8)
        self.shutdown_entry.place(x=70,y=30)
        self.shutdown_entry.insert(0,"7200")  # 默认值
        self.shutdowns_label = tk.Label(self.Part2_frame, text="秒")
        self.shutdowns_label.place(x=140,y=30)

        self.part2set_button = tk.Button(self.Part2_frame, text="设置", width=8, command=lambda:self.SetParas(4))
        self.part2set_button.place(x=170,y=20) 

        #Part 4
        self.SetAllParas_button = tk.Button(self.frame, text="设置全部参数", width=30, command=lambda:self.SetParas(5))
        self.SetAllParas_button.place(x=450,y=80)        

        self.ResetParas_button = tk.Button(self.frame, text="恢复默认设置", width=30, command=lambda:self.SetParas(6))
        self.ResetParas_button.place(x=450,y=120)

        #黑标设置
        self.blackmark_frame = ttk.LabelFrame(self.frame, text="黑标设置",width=680,height=100)
        self.blackmark_frame.place(x=0,y=175)   
        
             
    def SetParas(self,Num):
        print(f"num={Num}")
if __name__ == "__main__":
    root = tk.Tk()
    app = Paras_Set(root)
    root.mainloop()