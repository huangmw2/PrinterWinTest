#Paras Test
import tkinter as tk
from tkinter import ttk
from enum import Enum
import struct

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
    USB_INTERFACE_TYPE = 15
    PAPER_TYPE = 16
    PRINTER_ORDER = 17
    RECYCLE_TIME = 18
    PAPER_RULES = 19
    DESITY_LEVEL= 20
    FEED_PAPER_SWITCH = 21
    PRINTER_PROTOCOL = 22
    PAPER_JAM_SWITCH = 23
    PRINTER_SPEED = 24
    DEVICE_NAME = 25

class Paras_Set:
    def __init__(self,parent):
        self.frame =tk.Frame(parent,bd=2,relief=tk.GROOVE)
        self.frame.pack(fill=tk.BOTH,expand=True)
        if __name__ == "__main__":
            self.root = parent
            self.root.title("参数设置")
            self.root.geometry("700x500+600+300")    

        self.baud_rate_value = ["1200","2400","4800","9600", "19200", "38400", "57600", "115200","230400"]
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
            "ISO-8859-2:Latin2", "ISO-8859-3:Latin3", "ISO-8859-4:Baltic","ISO-8859-5:Cyrillic",
            "ISO-8859-6:Arabic", "ISO-8859-7:Greek", "ISO-8859-8:Hebrew", "ISO-8859-9:Turkish", 
            "ISO-8859-15:Latin3", "Thai2", "CP856:Hebrew", "CP874:Thai", "EUC-KR", "UTF-8"
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

        self.languge_entry = ttk.Combobox(self.Basic_frame, values=self.language_entry_value, state="readonly",width=20)
        self.languge_entry.place(x=50,y=85)
        self.languge_entry.set("CP936:GBK")  # 默认值
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
        self.SetAllParas_button.config(state='disabled')
        self.ResetParas_button = tk.Button(self.frame, text="恢复默认设置", width=30, command=lambda:self.SetParas(button_fun.RESET_FUN))
        self.ResetParas_button.place(x=450,y=120)

        #黑标设置
        self.blackmark_frame = ttk.LabelFrame(self.frame, text="黑标设置",width=550,height=120)
        self.blackmark_frame.place(x=0,y=175)   
        self.blackmark_frame.grid_propagate(False)

        #查找距离
        self.black_mark_dis = "300"
        self.black_mark_dis_entry = self.create_label_entry_button(self.blackmark_frame, 0,"黑标查找距离", self.black_mark_dis, "mm", "设置",lambda:self.SetParas(button_fun.BLACK_DISTAN_FUN))
        #黑标宽度
        self.black_mark_width = "40"
        self.black_mark_width_entry = self.create_label_entry_button(self.blackmark_frame,1, "黑标宽度", self.black_mark_width, "mm", "设置",lambda:self.SetParas(button_fun.BLACK_WIDTH_FUN))    
        #黑标宽度
        self.black_mark_feed = "40"
        self.black_mark_feed_entry = self.create_label_entry_button(self.blackmark_frame,2, "找到黑标后进纸", self.black_mark_feed, "mm", "设置",lambda:self.SetParas(button_fun.BLACK_FEED_FUN))    
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
        self.USBTypeCombobox = self.create_label_Combobox_button(self.product_frame,0,0,"USB 设备类型",self.USBType,self.USBType[0],"设置",lambda:self.SetParas(button_fun.USB_INTERFACE_TYPE))
        #纸张类型
        self.PaperType = ["热敏票据纸","热敏标签纸","热敏孔洞纸","热敏黑标纸"]
        self.PaperTypeCombobox = self.create_label_Combobox_button(self.product_frame,1,0,"纸张类型",self.PaperType,self.PaperType[0],"设置",lambda:self.SetParas(button_fun.PAPER_TYPE))
        #打印顺序
        self.PrintOrder = ["倒叙","正序"]
        self.PrintOrderCombobox =  self.create_label_Combobox_button(self.product_frame,2,0,"打印顺序",self.PrintOrder,self.PrintOrder[0],"设置",lambda:self.SetParas(button_fun.PRINTER_ORDER))
        #票据回收时间
        self.RecytingTime = ["2","5","10","15","20","30","60"]
        self.RecytingTimeCombobox = self.create_label_Combobox_button(self.product_frame,3,0,"票据回收时间",self.RecytingTime,self.RecytingTime[1],"设置",lambda:self.SetParas(button_fun.RECYCLE_TIME))
        #纸张规则
        self.PaperFormat = ["1寸","2寸","3寸","4寸"]
        self.PaperFormatCombobox = self.create_label_Combobox_button(self.product_frame,4,0,"纸张规则",self.PaperFormat,self.PaperFormat[2],"设置",lambda:self.SetParas(button_fun.PAPER_RULES))
        #浓度等级
        self.Desitylevel = ["浓度等级1","浓度等级2","浓度等级3","浓度等级4","浓度等级5","浓度等级6","浓度等级7","浓度等级8"]
        self.DesitylevelCombobox = self.create_label_Combobox_button(self.product_frame,0,3,"浓度等级",self.Desitylevel,self.Desitylevel[3],"设置",lambda:self.SetParas(button_fun.DESITY_LEVEL))
        #走纸键
        self.FeedPaperKey = ["关闭","开启"]
        self.FeedPaperKeyCombobox=self.create_label_Combobox_button(self.product_frame,1,3,"走纸键",self.FeedPaperKey,self.FeedPaperKey[0],"设置",lambda:self.SetParas(button_fun.FEED_PAPER_SWITCH))
        #打印机协议
        self.PrintProcotol = ["ESC","TSPL","CPCL","JPL"]
        self.PrintProcotolCombobox=self.create_label_Combobox_button(self.product_frame,2,3,"打印机协议",self.PrintProcotol,self.PrintProcotol[0],"设置",lambda:self.SetParas(button_fun.PRINTER_PROTOCOL))
        #堵纸侦测
        self.PaperJam = ["关闭","开启"]
        self.PaperJamCombobox=self.create_label_Combobox_button(self.product_frame,3,3,"堵纸侦测",self.PaperJam,self.PaperJam[0],"设置",lambda:self.SetParas(button_fun.PAPER_JAM_SWITCH))   
        #打印速度
        self.PrintSpeed = ["1","2","3","4","5","6","7","8"]
        self.PrintSpeedCombobox=self.create_label_Combobox_button(self.product_frame,4,3,"打印速度",self.PrintSpeed,self.PrintSpeed[0],"设置",lambda:self.SetParas(button_fun.PRINTER_SPEED))     

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

        self.deveice_button = tk.Button(self.devicename_frame, text="设置",command=lambda:self.SetParas(button_fun.DEVICE_NAME),width=12)
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

        return entry       
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

        return Combobox
    #Data Packet 发送的数据包 (组包)
    def Send_Packaging(self,_Command,_Paramh,_Paraml,Data=None,_StandordPro=True):
        if _StandordPro == False:
            Packet = Data
            packet_str = ' '.join(f'{byte:02x}' for byte in Packet)
            print(f"Packet={packet_str}")     
            return      
        #包头 + 起始标志位
        Start_flag = b'\x02\x00'
        #命令,2字节，小端
        Command = struct.pack('<H', _Command) #小端格式的命令
        #命令参数，高字节
        Param_h = _Paramh
        #命令参数，低字节
        Param_l = _Paraml
        #设备ID值
        Device_Id = b'\x00\x00\x00\x00'
        #数据长度
        if Data != None:
            _Data_length = len(Data)
            Data_length = struct.pack('<H', _Data_length)  # 小端格式的数据长度
        else :
            Data_length = b'\x00\x00'
        #计算校验和
        CheckSum = Start_flag[0] ^ Start_flag[1] ^ Command[0] ^ Command[1]
        CheckSum ^= Param_h[0] ^ Param_h[1] ^ Param_l[0] ^ Param_l[1]
        CheckSum ^= Device_Id[0] ^ Device_Id[1] ^ Device_Id[0] ^ Device_Id[1]
        CheckSum ^= Data_length[0] ^ Data_length[1]
        #预留位
        Reserved = b'\00'
        #数据校验和
        if Data != None:
            Data_CheckSum = 0
            for byte in Data:
                Data_CheckSum ^= byte   
            Packet = Start_flag + Command + Param_h + Param_l + Device_Id + Data_length + bytes([CheckSum]) + Reserved + Data + bytes([Data_CheckSum])
        else :
            Packet = Start_flag + Command + Param_h + Param_l + Device_Id + Data_length + bytes([CheckSum]) + Reserved
        #数据包
        packet_str = ' '.join(f'{byte:02x}' for byte in Packet)
        print(f"Packet={packet_str}")
    #连通数据
    def Connect_testing(self):
        Command = 0x30
        Paramh = b'\x00\x00'
        Paraml = b'\x00\x00'
        Data = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]
        Data = bytes(Data)
        return Command,Paramh,Paraml,Data
    #波特率设置数据
    def BaudRate_set(self):
        ChangeData = {
            '1200': "05",
            '2400': "06",
            '4800': "07",
            '9600': "00",
            '19200': "01",
            '38400': "02",
            '57600': "03",
            '115200': "04", 
            '230400': "08",          
        }
        Command = 0x81
        Paramh = b'\x00\x00'
        Paraml = b'\x00\x00'
        Old_BaudRate = self.baud_rate.get()
        New_BaudRate = ChangeData.get(Old_BaudRate, "00")
        Data = bytes.fromhex(New_BaudRate)
        return Command,Paramh,Paraml,Data
    #流控设置
    def Flow_set(self):
        ChangeData = {
            '硬件流控': "01",
            '软件流控': "00",         
        }
        Command = 0x8d
        Paramh = b'\x00\x00'
        Paraml = b'\x00\x00'
        Old_Data = self.flow_control.get()
        New_Data = ChangeData.get(Old_Data, "00")
        Data = bytes.fromhex(New_Data)
        return Command,Paramh,Paraml,Data
    #语言设置
    def Language_set(self):
        ChangeData = {
            "CP932 SHIFT JIS": "fc",
            "UNICODE UCS-2": "fd",
            "CP950:BIG5": "fe",
            "CP936:GBK": "ff",
            "CP437:USA/Standard Europe": "00",
            "Katakana": "01",
            "CP850:Latin1;Western European": "02",
            "CP860:Portuguese": "03",
            "CP863:French Canadian": "04",
            "CP865:Nordic": "05",
            "CP1251:Cyrillic": "06",
            "CP866:Russian;Cyrillic": "07",
            "CP1025:Cyrillic/Bulgarian": "08",
            "CP773:Estonian/Lithuanian/Latvian": "09",
            "Iran": "0a",
            "Reversed": "0b",
            "CP862:Hebrew": "0f",
            "CP1252:Latin1": "10",
            "CP1253:Greek": "11",
            "CP852:Latin2": "12",
            "CP858:Latin1+Euro": "13",
            "Iran II": "14",
            "CP1117:Latvian": "15",
            "CP864:Arabic": "16",
            "ISO-8859-1:West Europe": "17",
            "CP737:Greek": "18",
            "CP1257:Baltic": "19",
            "Thai": "1a",
            "CP720:Arabic": "1b",
            "CP855:Cyrillic": "1c",
            "CP857:Turkish": "1d",
            "CP1250:Central Europe": "1e",
            "CP775:Estonian/Lithuanian/Latvian": "1f",
            "CP1254:Turkish": "20",
            "CP1255:Hebrew": "21",
            "CP1256:Arabic": "22",
            "CP1258:Vietnam": "23",
            "ISO-8859-2:Latin2": "24",
            "ISO-8859-3:Latin3": "25",
            "ISO-8859-4:Baltic": "26",
            "ISO-8859-5:Cyrillic":"27",
            "ISO-8859-6:Arabic": "28",
            "ISO-8859-7:Greek": "29",
            "ISO-8859-8:Hebrew": "2a",
            "ISO-8859-9:Turkish": "2b",
            "ISO-8859-15:Latin3": "2c",
            "Thai2": "2d",
            "CP856:Hebrew": "2e",
            "CP874:Thai": "2f",
            "EUC-KR": "fa",
            "UTF-8": "fb"
        }

        Command = 0x80
        Paramh = b'\x00\x00'
        Paraml = b'\x00\x00'
        Old_Data = self.languge_entry.get()
        New_Data = ChangeData.get(Old_Data, "00")
        Data = bytes.fromhex(New_Data)
        return Command,Paramh,Paraml,Data      
    #集合参数1设置
    def Part1_set(self):
        ChangeData1 = {
            '9x17': "00",
            '12x24': "40",         
            '9x24': "08",
            '16x18': "48",   
        }
        ChangeData2 = {
            '微淡': "00",
            '正常': "80",         
            '微浓': "01",
            '高浓': "81",   
        }
        ChangeData3 = {
            '0x0A': "00",
            '0x0D': "01",              
        }
        ChangeData4 = {
            '不切': "00",
            '最后一张切': "01", 
            '指令切': "02", 
            '单张切': "03",              
        }
        
        
        Command = 0x82
        Paramh = b'\x00\x00'
        Paraml = b'\x00\x00'
        #字体
        Temp = self.font_size.get()
        Temp = ChangeData1.get(Temp, "40")
        Temp = int(Temp,16)
        Old_Data1 = Temp
        #浓度
        Temp = self.print_density.get()
        Temp = ChangeData2.get(Temp, "80")
        Temp = int(Temp,16)
        Old_Data1 += Temp
        #切刀
        if self.buzzer_var.get():
            Old_Data1 += 0x04
        #蜂鸣器
        if self.knife_var.get():
            Old_Data1 += 0x20
        New_Data1 = Old_Data1.to_bytes(1, byteorder='little')


        Old_Data2 = self.paper_feed.get()
        New_Data2 = ChangeData3.get(Old_Data2, "00")
        New_Data2 = bytes.fromhex(New_Data2)

        Old_Data3 = self.cutter_type.get()
        New_Data3 = ChangeData4.get(Old_Data3, "00")
        New_Data3 = bytes.fromhex(New_Data3)

        Data = New_Data1 + New_Data2 + New_Data3
        return Command,Paramh,Paraml,Data  
    #休眠时间设置
    def Sleep_set(self):
        Command = 0x86
        Paramh = b'\x00\x00'
        Paraml = b'\x00\x00'

        sleep_time = int(self.sleep_entry.get())
        sleep_time = sleep_time.to_bytes(4, byteorder='little')

        shut_time = int(self.shutdown_entry.get())
        shut_time = shut_time.to_bytes(4, byteorder='little')

        Data = sleep_time + shut_time
        return Command,Paramh,Paraml,Data
    #设置全部参数
    def All_Set(self):
        pass
    
    #恢复出场设置
    def Reset_set(self):
        Command = 0x79
        Paramh = b'\x00\x00'
        Paraml = b'\x00\x00'
        Data = None
        return Command,Paramh,Paraml,Data
    #黑标设置:非统一指令
    def Black_set(self):
        Data = "1f 1b 1f 80 04 05 06 44"
        return bytes.fromhex(Data)
    def Black_cancel(self):
        Data = "1f 1b 1f 80 04 05 06 66"
        return bytes.fromhex(Data)
    def Black_distance(self):
        Cmd = "1f 1b 1f 81 04 05 06"
        Value = int(self.black_mark_dis_entry.get())
        Data = bytes.fromhex(Cmd) + Value.to_bytes(2, byteorder='big')
        return Data
    def Black_Width(self):
        Cmd = "1f 1b 1f 82 04 05 06"
        Value = int(self.black_mark_width_entry.get())
        Data = bytes.fromhex(Cmd) + Value.to_bytes(2, byteorder='big')
        return Data
    def Black_Feed(self):
        Cmd = "1d 28 46 04 00 01 00"
        Value = int(self.black_mark_feed_entry.get())
        Data = bytes.fromhex(Cmd) + Value.to_bytes(2, byteorder='little')
        return Data
    def Black_Find(self):
        Cmd = "0c"
        Data = bytes.fromhex(Cmd)
        return Data
    def Black_FindCut(self):
        Cmd = "0c 1b 69"
        Data = bytes.fromhex(Cmd)
        return Data
    def Black_PrintCut(self):
        PrintData = """02 00 30 00  00 00 00 00  00 00 00 00  04 00 36 00  41 39 00 01  79
        02 00 30 00  00 00 00 00  00 00 00 00  08 00 3a 00  01 02 04 08  10 20 40 80  ff
        1b 40 1b 61  01 1b 21 00  57 65 6c 63  6f 6d 65 20  74 6f 20 70  72 69 6e 74  65 72 20 42  6c 61 63 6b
        4d 61 72 6b  20 66 75 6e  63 74 69 6f  6e 0d 0a 1b  39 00 bb b6  d3 ad ca b9  d3 c3 ba da  b1 ea b9 a6
        c4 dc 0d 0a  1b 39 03 c5  77 aa ef a8  cf a5 ce b6  c2 bc d0 a5  5c af e0 0d  0a 1d 28 6b  03 00 31 43
        04 1d 28 6b  03 00 31 45  30 1d 28 6b  72 00 31 50  30 57 65 6c  63 6f 6d 65  20 74 6f 20  70 72 69 6e
        74 65 72 20  42 6c 61 63  6b 4d 61 72  6b 20 66 75  6e 63 74 69  6f 6e 0a e6  ac a2 e8 bf  8e e4 bd bf
        e7 94 a8 e6  89 93 e5 8d  b0 e6 9c ba  e7 9a 84 e9  bb 91 e6 a0  87 e5 8a 9f  e8 83 bd 0a  e6 ad a1 e8
        bf 8e e4 bd  bf e7 94 a8  e5 8d b0 e8  a1 a8 e6 a9  9f e7 9a 84  e9 bb 91 e6  a8 99 e5 8a  9f e8 83 bd
        1d 28 6b 03  00 31 51 30  0c 1b 69""" 
        Data = bytes.fromhex(PrintData)
        return Data
    #产品设置
    def Usb_TypeSet(self):
        Value = self.USBTypeCombobox.get()
        ChangeData = {
            '打印口': "12 55 01",
            '虚拟串口': "12 55 00",          
        }
        Data = ChangeData.get(Value, "12 55 01")
        return bytes.fromhex(Data)
    #纸张类型
    def Paper_TypeSet(self):
        Value = self.PaperTypeCombobox.get()
        ChangeData = {
            '热敏票据纸': "1f 41 00",
            '热敏标签纸': "1f 41 01",
            '热敏孔洞纸': "1f 41 02", 
            '热敏黑标纸': "1f 41 03",          
        }
        Data = ChangeData.get(Value, "1f 41 00")
        return bytes.fromhex(Data)    
    #["倒叙","正序"]
    def Print_OrderSet(self):
        Value = self.PrintOrderCombobox.get()
        ChangeData = {
            '倒叙': "1b 70 f1",
            '正序': "1b 70 f0",      
        }
        Data = ChangeData.get(Value, "1b 70 f0")
        return bytes.fromhex(Data) 
    #票据回收时间 ["2","5","10","15","20","30","60"]
    def RecytingTime_Set(self):
        ChangeData = {
            '2': "02",
            '5': "05",     
            '10': "0a",
            '15': "0f",  
            '20': "14",
            '30': "1e",   
            '60': "3c",  
        }
        Command = 0x8c
        Paramh = b'\x00\x00'
        Paraml = b'\x00\x00'
        Old_Data = self.RecytingTimeCombobox.get()
        New_Data = ChangeData.get(Old_Data, "02")
        Data = bytes.fromhex(New_Data)
        return Command,Paramh,Paraml,Data
    #纸张大小["1寸","2寸","3寸","4寸"]
    def PaperFormat_Set(self):
        ChangeData = {
            '1寸': "03",
            '2寸': "00",     
            '3寸': "01",
            '4寸': "02",    
        }
        Command = 0x90
        Paramh = b'\x00\x00'
        Paraml = b'\x00\x00'
        Old_Data = self.PaperFormatCombobox.get()
        New_Data = ChangeData.get(Old_Data, "01")
        Data = bytes.fromhex(New_Data)
        return Command,Paramh,Paraml,Data
    #浓度等级  ["浓度等级1","浓度等级2","浓度等级3","浓度等级4","浓度等级5","浓度等级6","浓度等级7","浓度等级8"]
    def Desitylevel_Set(self):
        ChangeData = {
            '浓度等级1': "80 01",
            '浓度等级2': "80 02",     
            '浓度等级3': "80 03",
            '浓度等级4': "80 04",  
            '浓度等级5': "80 05",
            '浓度等级6': "80 06",     
            '浓度等级7': "80 07",
            '浓度等级8': "80 08",   
        }
        Command = 0x92
        Paramh = b'\x00\x00'
        Paraml = b'\x00\x00'
        Old_Data = self.DesitylevelCombobox.get()
        New_Data = ChangeData.get(Old_Data, "80 04")
        Data = bytes.fromhex(New_Data)
        return Command,Paramh,Paraml,Data
    # ["关闭","开启"]
    def FeedPaperKey_Set(self):
        Value = self.FeedPaperKeyCombobox.get()
        ChangeData = {
            '关闭': "1b 63 35 f1",
            '开启': "1b 63 35 f0",          
        }
        Data = ChangeData.get(Value, "1b 63 35 f0")
        return bytes.fromhex(Data)
    #打印机协议  ["ESC","TSPL","CPCL","JPL"]
    def PrintProcotol_Set(self):
        ChangeData = {
            'ESC': "82 00",
            'TSPL': "82 01",   
            'CPCL': "82 02",
            'JPL': "82 03",         
        }
        Command = 0x92
        Paramh = b'\x00\x00'
        Paraml = b'\x00\x00'
        Old_Data = self.PrintProcotolCombobox.get()
        New_Data = ChangeData.get(Old_Data, "82 00")
        Data = bytes.fromhex(New_Data)
        return Command,Paramh,Paraml,Data 
    
    # 堵纸侦测
    def PaperJam_Set(self):
        ChangeData = {
            '关闭': "84 00",
            '开启': "84 01",           
        }
        Command = 0x92
        Paramh = b'\x00\x00'
        Paraml = b'\x00\x00'
        Old_Data = self.PaperJamCombobox.get()
        New_Data = ChangeData.get(Old_Data, "84 00")
        Data = bytes.fromhex(New_Data)
        return Command,Paramh,Paraml,Data 
    # 打印速度
    def PrintSpeed_Set(self):
        ChangeData = {
            '1': "83 01",
            '2': "83 02", 
            '3': "83 03",
            '4': "83 04",
            '5': "83 05",
            '6': "83 06",
            '7': "83 07",
            '8': "83 08",          
        }
        Command = 0x92
        Paramh = b'\x00\x00'
        Paraml = b'\x00\x00'
        Old_Data = self.PrintSpeedCombobox.get()
        New_Data = ChangeData.get(Old_Data, "83 05")
        Data = bytes.fromhex(New_Data)
        return Command,Paramh,Paraml,Data 
    #产品设置
    def Product_set(self):
        Command = 0x85
        Paramh = b'\x00\x00'
        Paraml = b'\x00\x00'
        Name = self.decicename_lentry.get()
        hex_string = Name.encode('utf-8').hex()
        if len(hex_string) < 40:
            hex_string = hex_string.ljust(40, '0')  # 用'0'填充到40个字符
        Data1 = bytes.fromhex(hex_string)   

        Number = self.decicenum_lentry.get()
        hex_string = Number.encode('utf-8').hex()
        if len(hex_string) < 40:
            hex_string = hex_string.ljust(40, '0')  # 用'0'填充到40个字符
        Data2 = bytes.fromhex(hex_string) 

        Data = Data1 + Data2
        return Command,Paramh,Paraml,Data 
    
    def SetParas(self,Num):
        StandorPro = False
        if Num.value in(7,8,9,10,11,12,13,14,15,16,17,21):
            StandorPro = False
        else :
            StandorPro = True
     
        callback_fun = {
            button_fun.BAUD_RATE_FUN.value:self.BaudRate_set(),
            button_fun.FLOW_FUN.value:self.Flow_set(),
            button_fun.LANGUGE_FUN.value:self.Language_set(),
            button_fun.PART1_FUN.value:self.Part1_set(),
            button_fun.PART2_FUN.value:self.Sleep_set(),
            button_fun.SETALL_FUN.value:self.All_Set(),
            button_fun.RESET_FUN.value:self.Reset_set(),
            button_fun.BLACK_DISTAN_FUN.value:self.Black_distance(),
            button_fun.BLACK_WIDTH_FUN.value:self.Black_Width(),
            button_fun.BLACK_FEED_FUN.value:self.Black_Feed(),
            button_fun.BLACK_ENABLE_FUN.value:self.Black_set(),
            button_fun.BLACK_DISABILITY_FUN.value:self.Black_cancel(),
            button_fun.BLACK_FIND_FUN.value:self.Black_Find(),
            button_fun.BLACK_FINDCUT_FUN.value:self.Black_FindCut(),
            button_fun.BLACK_PRINTTEST_FUN.value:self.Black_PrintCut(),
            button_fun.USB_INTERFACE_TYPE.value:self.Usb_TypeSet(),
            button_fun.PAPER_TYPE.value:self.Paper_TypeSet(),
            button_fun.PRINTER_ORDER.value:self.Print_OrderSet(),
            button_fun.RECYCLE_TIME.value:self.RecytingTime_Set(),
            button_fun.PAPER_RULES.value:self.PaperFormat_Set(),
            button_fun.DESITY_LEVEL.value:self.Desitylevel_Set(),
            button_fun.FEED_PAPER_SWITCH.value:self.FeedPaperKey_Set(),
            button_fun.PRINTER_PROTOCOL.value:self.PrintProcotol_Set(),
            button_fun.PAPER_JAM_SWITCH.value:self.PaperJam_Set(),
            button_fun.PRINTER_SPEED.value:self.PrintSpeed_Set(),
            button_fun.DEVICE_NAME.value:self.Product_set(),
        }
        func = callback_fun.get(Num.value, None)

        Command = 0x00
        Paramh = b'\x00\x00'
        Paraml = b'\x00\x00'
        Data   = []
        
        if StandorPro:
            Command,Paramh,Paraml,Data = func
        else :
            Data = func

        self.Send_Packaging(Command,Paramh,Paraml,Data,StandorPro)    
            


if __name__ == "__main__":
    root = tk.Tk()
    app = Paras_Set(root)
    root.mainloop()