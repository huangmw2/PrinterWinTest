# RAM Test
import tkinter as tk
from tkinter import ttk
import time
import struct
if __name__ == "__main__":
    from Config import Config_Data
    from Queue import queue_handler
else :
    from APP.Config import Config_Data
    from APP.Queue import queue_handler

class RAM_Test:
    def __init__(self,parent):
        self.frame = tk.Frame(parent,bd=2,relief=tk.GROOVE)
        self.frame.pack(fill=tk.BOTH,expand=True)
        if __name__ == "__main__":
            self.root = parent
            self.root.title("自定义参数设置")
            self.root.geometry("700x500+600+300")
        self.ConfigData = Config_Data.Get_Data()

        self.Fun_frame = ttk.LabelFrame(self.frame,text="功能区")
        self.Fun_frame.place(x=0,y=0,width=350,height=400)
        
        self.canvas = tk.Canvas(self.Fun_frame)
        self.scrollbar = ttk.Scrollbar(self.Fun_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        # 绑定滚动区域
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # 布局滚动条和画布
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.place(x=330,y=0,height=400)

        #按钮
        self.Add_DiyParas = tk.Button(self.frame, text="添加自定义参数",command=self.Add_Paras,width=13,font=("仿宋",11,"bold"))
        self.Add_DiyParas.place(x=30,y=410) 

        self.Save_DiyParas = tk.Button(self.frame, text="保存数据",command=self.Save_Paras,width=10,font=("仿宋",11,"bold"))
        self.Save_DiyParas.place(x=210,y=410)

        self.Entry_1 = []
        self.Entry_2 = []
        self.Diy_paras()

    def Diy_paras(self):
        Diy_Dat = self.ConfigData["Diy_Paras"]
        Diy_Cnt = len(self.ConfigData["Diy_Paras"])
        # 获取第一个节点的名称和值
        for i in range(Diy_Cnt):
            key = list(Diy_Dat.keys())[i]  # 获取第一个键
            value = Diy_Dat[key]    # 根据键获取对应的值
            self.creat_entry_entry_button(self.scrollable_frame,i,key,value,lambda i=i:self.Send_button(i))

    def creat_entry_entry_button(self,frame,_row,text1,cmd,button_fun): 
        entry_1 = tk.Entry(frame, width=13)
        entry_1.grid(row=_row, column=0, padx=5, pady=2,sticky="w")
        entry_1.insert(0,text1)
        self.Entry_1.append(entry_1)

        entry_2 = tk.Entry(frame, width=13)
        entry_2.grid(row=_row, column=1, padx=5, pady=2,sticky="w")
        entry_2.insert(0,cmd)     
        self.Entry_2.append(entry_2)

        button = tk.Button(frame, text="发送",command=button_fun,width=8)
        button.grid(row=_row, column=2, padx=5, pady=1)          

        #return entry_1,entry_2
    
    def Send_button(self,Value):
        #连接通信测试
        testcmd, testdata = self.Connect_testing()
        self.Send_Packaging(testcmd,testdata,"连接测试")
        #发送对应设置指令
        byte_data = bytes.fromhex(self.Entry_2[Value].get())
        Name = "设置参数{}",format(self.Entry_1[Value].get())
        self.Send_Packaging(0x92,byte_data,Name)

    def Add_Paras(self):
        _row = len(self.Entry_1)
        self.creat_entry_entry_button(self.scrollable_frame,_row,"","",lambda:self.Send_button(_row))

    def Save_Paras(self):
        Updated_data = {}
        n = len(self.Entry_1)
        for  i  in range(n):
            key = self.Entry_1[i].get()  # 从第一个 Entry 中获取键
            value = self.Entry_2[i].get()  # 从第二个 Entry 中获取值
            # 如果键和值都为空，则跳过
            if not key and not value:
                continue
            Updated_data[key] = value  # 将键值对存入字典    
        ret = Config_Data.Modify_Data("Diy_Paras",value=Updated_data)
        if ret == True:
            Config_Data.Save_Data()
    #Data Packet 发送的数据包 (组包)
    def Send_Packaging(self,_Command,Data=None,Name=" "): 
        #包头 + 起始标志位
        Start_flag = b'\x02\x00'
        #命令,2字节，小端
        Command = struct.pack('<H', _Command) #小端格式的命令
        Param_h = b'\x00\x00'
        Param_l = b'\x00\x00'
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
        #hex_string_with_space = ' '.join(f'{byte:02x}' for byte in Packet)
        #print(hex_string_with_space)
        queue_handler.write_to_queue(Packet,Name)  

    #连通数据
    def Connect_testing(self):
        Command = 0x30
        Data = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]
        Data = bytes(Data)
        return Command,Data
    
if __name__ == "__main__":
    root = tk.Tk()
    app = RAM_Test(root)
    root.mainloop()