#Paras Test
import tkinter as tk
from tkinter import ttk
from enum import Enum


class button_fun(Enum):
    BAUD_RATE_FUN = 0
    FLOW_FUN = 1
    LANGUGE_FUN = 2
    PART1_FUN = 3
    PART2_FUN = 4
    SETALL_FUN = 5
    RESET_FUN = 6
    BLACK_DISTAN_FUN = 7
    BLACK_WIDTH_FUN =8
    BLACK_FEED_FUN = 9
    BLACK_ENABLE_FUN =10
    BLACK_DISABILITY_FUN = 11
    BLACK_FIND_FUN = 12
    BLACK_FINDCUT_FUN = 13
    BLACK_PRINTTEST_FUN =14

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

        set_button = tk.Button(self.Basic_frame, text="设置", width=8, command=lambda:self.SetParas(button_fun.BAUD_RATE_FUN))
        set_button.place(x=150,y=0)   
        #流控
        self.flow_label = tk.Label(self.Basic_frame, text="流控:")
        self.flow_label.place(x=0,y=45)

        self.flow_control = ttk.Combobox(self.Basic_frame, values=self.flow_control_value, state="readonly",width=10)
        self.flow_control.place(x=50,y=45)
        self.flow_control.set("硬件流控")  # 默认值
        set_flow_button = tk.Button(self.Basic_frame, text="设置", width=8, command=lambda:self.SetParas(button_fun.FLOW_FUN))
        set_flow_button.place(x=150,y=40)   
        #流控
        self.languge_label = tk.Label(self.Basic_frame, text="语言:")
        self.languge_label.place(x=0,y=85)

        self.languge_entry = encoding = ttk.Combobox(self.Basic_frame, values=self.language_entry_value, state="readonly",width=20)
        self.languge_entry = encoding.place(x=50,y=85)
        self.languge_entry = encoding.set("UTF-8")  # 默认值
        self.set_languge_button = tk.Button(self.Basic_frame, text="设置", width=8, command=lambda:self.SetParas(button_fun.LANGUGE_FUN))
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

        self.partset_button = tk.Button(self.Part_frame, text="设置", width=8, command=lambda:self.SetParas(button_fun.PART1_FUN))
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

        self.part2set_button = tk.Button(self.Part2_frame, text="设置", width=8, command=lambda:self.SetParas(button_fun.PART2_FUN))
        self.part2set_button.place(x=170,y=20) 

        #Part 4
        self.SetAllParas_button = tk.Button(self.frame, text="设置全部参数", width=30, command=lambda:self.SetParas(button_fun.SETALL_FUN))
        self.SetAllParas_button.place(x=450,y=80)        

        self.ResetParas_button = tk.Button(self.frame, text="恢复默认设置", width=30, command=lambda:self.SetParas(button_fun.RESET_FUN))
        self.ResetParas_button.place(x=450,y=120)

        #黑标设置
        self.blackmark_frame = ttk.LabelFrame(self.frame, text="黑标设置",width=550,height=120)
        self.blackmark_frame.place(x=0,y=175)   
        self.blackmark_frame.grid_propagate(False)

        #查找距离
        self.black_mark_dis = "300"
        self.create_label_entry_button(self.blackmark_frame, 0,"黑标查找距离", self.black_mark_dis, "mm", "设置",lambda:self.SetParas(button_fun.BLACK_DISTAN_FUN))
        #黑标宽度
        self.black_mark_width = "40"
        self.create_label_entry_button(self.blackmark_frame,1, "黑标宽度", self.black_mark_width, "mm", "设置",lambda:self.SetParas(button_fun.BLACK_WIDTH_FUN))    
        #黑标宽度
        self.black_mark_feed = "40"
        self.create_label_entry_button(self.blackmark_frame,2, "找到黑标后进纸", self.black_mark_feed, "mm", "设置",lambda:self.SetParas(button_fun.BLACK_FEED_FUN))    
        #设置黑标模式
        self.Create_black_button(self.blackmark_frame ,"设置黑标模式", 300,10,lambda:self.SetParas(button_fun.BLACK_ENABLE_FUN))         
        #取消黑标模式
        self.Create_black_button(self.blackmark_frame ,"取消黑标模式", 300,50,lambda:self.SetParas(button_fun.BLACK_DISABILITY_FUN))   
        #查找黑标
        self.Create_black_button(self.blackmark_frame ,"查找黑标", 420,5,lambda:self.SetParas(button_fun.BLACK_FIND_FUN))   
        #查找黑标并切纸
        self.Create_black_button(self.blackmark_frame ,"查找黑标并切纸", 420,32,lambda:self.SetParas(button_fun.BLACK_FINDCUT_FUN))    
        #打印测试
        self.Create_black_button(self.blackmark_frame ,"打印测试", 420,60,lambda:self.SetParas(button_fun.BLACK_PRINTTEST_FUN))

        #产品设置
        self.product_frame = ttk.LabelFrame(self.frame, text="产品设置",width=550,height=178)
        self.product_frame.place(x=0,y=295)   
        self.product_frame.grid_propagate(False)

        #USB 接口类型
        self.USBType = ["打印口","虚拟串口"]
        self.create_label_Combobox_button(self.product_frame,0,0,"USB 设备类型",self.USBType,self.USBType[0],"设置",lambda:self.SetParas(15))
        #纸张类型
        self.PaperType = ["热敏票据纸","热敏标签纸","热敏孔洞纸","热敏黑标纸"]
        self.create_label_Combobox_button(self.product_frame,1,0,"纸张类型",self.PaperType,self.PaperType[0],"设置",lambda:self.SetParas(16))
        #打印顺序
        self.PrintOrder = ["倒叙","正序"]
        self.create_label_Combobox_button(self.product_frame,2,0,"纸张类型",self.PrintOrder,self.PrintOrder[0],"设置",lambda:self.SetParas(17))
        #票据回收时间
        self.RecytingTime = ["2","5","10","15","20","30","60"]
        self.create_label_Combobox_button(self.product_frame,3,0,"票据回收时间",self.RecytingTime,self.RecytingTime[1],"设置",lambda:self.SetParas(18))
        #纸张规则
        self.PaperFormat = ["1寸","2寸","3寸","4寸"]
        self.create_label_Combobox_button(self.product_frame,4,0,"纸张规则",self.PaperFormat,self.PaperFormat[2],"设置",lambda:self.SetParas(19))
        #浓度等级
        self.Desitylevel = ["浓度等级1","浓度等级2","浓度等级3","浓度等级4","浓度等级5","浓度等级6","浓度等级7","浓度等级8"]
        self.create_label_Combobox_button(self.product_frame,0,3,"浓度等级",self.Desitylevel,self.Desitylevel[3],"设置",lambda:self.SetParas(20))
        #走纸键
        self.FeedPaperKey = ["关闭","开启"]
        self.create_label_Combobox_button(self.product_frame,1,3,"走纸键",self.FeedPaperKey,self.FeedPaperKey[0],"设置",lambda:self.SetParas(21))
        #打印机协议
        self.PrintProcotol = ["ESC","TSPL","CPCL"]
        self.create_label_Combobox_button(self.product_frame,2,3,"打印机协议",self.PrintProcotol,self.PrintProcotol[0],"设置",lambda:self.SetParas(22))
        #堵纸侦测
        self.PaperJam = ["关闭","开启"]
        self.create_label_Combobox_button(self.product_frame,3,3,"堵纸侦测",self.PaperJam,self.PaperJam[0],"设置",lambda:self.SetParas(23))   
        #打印速度
        self.PrintSpeed = ["1","2","3","4","5","6","7","8"]
        self.create_label_Combobox_button(self.product_frame,4,3,"打印速度",self.PrintSpeed,self.PrintSpeed[0],"设置",lambda:self.SetParas(24))     

        #设备名称
        self.devicename_frame = ttk.LabelFrame(self.frame, text="设备名称",width=150,height=175)
        self.devicename_frame.place(x=550,y=175)   
        self.devicename_frame.grid_propagate(False)

        self.decicename_label = tk.Label(self.devicename_frame, text="产品名称:")
        self.decicename_label.grid(row=0, column=0, padx=1, pady=2,sticky="w")

        self.decicename_lentry = tk.Entry(self.devicename_frame, width=18)
        self.decicename_lentry.grid(row=1, column=0, padx=1, pady=2,sticky="w")

        self.decicenum_label = tk.Label(self.devicename_frame, text="产品序列号:")
        self.decicenum_label.grid(row=3, column=0, padx=1, pady=2,sticky="w")

        self.decicenum_lentry = tk.Entry(self.devicename_frame, width=18)
        self.decicenum_lentry.grid(row=4, column=0, padx=1, pady=2,sticky="w")

        self.deveice_button = tk.Button(self.devicename_frame, text="设置",command=lambda:self.SetParas(25),width=12)
        self.deveice_button .grid(row=5, column=0, padx=1, pady=5) 

        #log区
        self.Log_frame = ttk.LabelFrame(self.frame, text="Log区",width=150,height=120)
        self.Log_frame.place(x=550,y=350)  

        self.Log_text = tk.Text(self.Log_frame, height=7, width=20)
        self.Log_text.place(x=0,y=0)
        # 禁止键盘输入的绑定
        self.Log_text.bind("<Key>", lambda e: "break")      
    # 创建一个统一的标签输入框和按钮布局
    def create_label_entry_button(self,frame,rows,label_text,entry_value,unit_text,button_text,butonn_fun):
 
        label = tk.Label(frame, text=label_text)
        label.grid(row=rows, column=0, padx=1, pady=1)

        entry = tk.Entry(frame, width=10)
        entry.insert(0, entry_value)
        entry.grid(row=rows, column=1, padx=1, pady=1)      

        unit_label = tk.Label(frame, text=unit_text)
        unit_label.grid(row=rows, column=2, padx=1, pady=1) 
        
        button = tk.Button(frame, text=button_text,command=butonn_fun,width=10)
        button.grid(row=rows, column=3, padx=1, pady=1) 
       
    def Create_black_button(self,frame,name,site_x,site_y,fun):
        button = tk.Button(frame, text=name,command=fun,font=("仿宋",10,"bold"))
        button.place(x=site_x,y=site_y) 

    # 创建一个统一的标签输入框和按钮布局
    def create_label_Combobox_button(self,frame,rows,columns,label_text,Combobox_value,default,button_text,butonn_fun):
 
        label = tk.Label(frame, text=label_text)
        label.grid(row=rows, column=columns+0, padx=5, pady=1,sticky="w")

        Combobox = ttk.Combobox(frame, values=Combobox_value, state="readonly",width=12)
        Combobox.grid(row=rows, column=columns+1, padx=5, pady=1)
        Combobox.set(default)  # 默认
        
        button = tk.Button(frame, text=button_text,command=butonn_fun,width=8)
        button.grid(row=rows, column=columns+2, padx=5, pady=1) 

    def SetParas(self,Num):
        print(f"num={Num.value}")
if __name__ == "__main__":
    root = tk.Tk()
    app = Paras_Set(root)
    root.mainloop()