#ESC Test.py
import os
import re
import time 
import struct
import tkinter as tk
from tkinter import ttk,filedialog,messagebox
from PIL import Image, ImageTk  # 如果没有安装PIL，可以通过 pip install pillow 安装
if __name__ == "__main__":
    from queue_manager import queue_handler
    from logger import log_message  
else :
    from APP.queue_manager import queue_handler
    from APP.logger import log_message 
import logging

class Esc_Test:
    def __init__(self,parent):

        self.parent = parent
        if __name__ == "__main__":
            self.root = parent
            self.root.title("ESC测试")
            self.root.geometry("700x500+600+300")
        
       #接收到的数据
        self.receiveStatus_array = []
        self.receiveId_array = []
        self.MonitorFlag = False
        self.MonitorIDFlag = False
       # self.parent = parent
        self.Image_DefaultPath = "./time.bmp"
        # 创建主框架
        self.frame = tk.Frame(parent, bd=2, relief=tk.GROOVE)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.DataPath_80mm = os.getcwd() + r"\Data\ESC\80mmReceipt.hex"
        self.DataPath_58mm = os.getcwd() + r"\Data\ESC\58mmReceipt.hex"
        # 发送区域
        send_frame = ttk.LabelFrame(self.frame, text="发送区")
        send_frame.grid(row=0, column=0, padx=1, pady=1, sticky="nsew")
        # 停止标志位
        self.stop_flag = False
        #临时数据
        self.Temp_data = None
        self.SentTimes = 0 #已经发送的次数
        # 创建滚动条
        send_scrollbar = ttk.Scrollbar(send_frame)
        send_scrollbar.grid(row=0, column=1, padx=1, pady=1,sticky='ns')
        # 创建文本框并绑定滚动条
        self.send_text = tk.Text(send_frame, height=10, width=50, yscrollcommand=send_scrollbar.set)
        self.send_text.grid(row=0, column=0, padx=1, pady=1)
        # 绑定滚动条到文本框
        send_scrollbar.config(command=self.send_text.yview)
        self.Hex_send_flag = tk.BooleanVar()
        self.Hex_send_flag.set(True)
        hex_send_check = tk.Checkbutton(send_frame, 
                                         text="十六进制发送",
                                         variable=self.Hex_send_flag,
                                         onvalue=True,
                                         offvalue=False,
                                         command=self.Hex_model,
                                         font=("仿宋",10))
        hex_send_check.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        open_button = ttk.Button(send_frame, text="打开文件", command=self.open_file)
        open_button.grid(row=1, column=0, padx=(120,0), pady=5, sticky="w")

        clear_send_button = ttk.Button(send_frame, text="清空发送区", command=lambda: self.send_text.delete(1.0, tk.END))
        clear_send_button.grid(row=1, column=0, padx=(200,0), pady=5)

        #接收区
        recv_frame = ttk.LabelFrame(self.frame,text="接收区")
        recv_frame.place(x=0,y=200,width=380,height=140)

        recv_scrollbar = ttk.Scrollbar(recv_frame)
        recv_scrollbar.grid(row=0, column=1, padx=1, pady=1,sticky='ns')
        # 创建文本框并绑定滚动条
        self.recv_text = tk.Text(recv_frame, height=6, width=50, yscrollcommand=recv_scrollbar.set)
        self.recv_text.grid(row=0, column=0, padx=1, pady=1)
        # 绑定滚动条到文本框
        recv_scrollbar.config(command=self.recv_text.yview)
        self.Hex_reve_flag = tk.BooleanVar()
        self.Hex_reve_flag.set(True)
        hex_recv_check = tk.Checkbutton(recv_frame, text="十六进制接收",
                                        variable=self.Hex_reve_flag,
                                        onvalue=True,
                                        offvalue=False,
                                        command=self.Hex_model,
                                        font=("仿宋",10))
        hex_recv_check.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        Clear_recv_button = ttk.Button(recv_frame, text="清空接收区", command=lambda: self.recv_text.delete(1.0, tk.END))
        Clear_recv_button.grid(row=1, column=0, padx=(120,0), pady=5,sticky="w")

        Status_Monitor_button = ttk.Button(recv_frame, text="状态检测", command=self.MonitorStatus)
        Status_Monitor_button.grid(row=1, column=0, padx=(200,0), pady=5)
        #功能区
        self.function_frame = ttk.LabelFrame(self.frame,text="功能区")
        self.function_frame.place(x=0,y=345,width=380,height=140)
        self.Send_loop = tk.BooleanVar()
        self.Send_loop.set(False)
        self.Loop_send_check = tk.Checkbutton(self.function_frame, 
                                         text="定时发送",
                                         variable=self.Send_loop,
                                         onvalue=True,
                                         offvalue=False,
                                         command=self.Loop_send,
                                         font=("仿宋",10))
        
        self.Loop_send_check.grid(row=0, column=0, padx=5, pady=5, sticky="w")   
        self.Send_times_entry = tk.Entry(self.function_frame,width=7)
        self.Send_times_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.Send_times_entry.insert(0,"100")

        self.Send_times_label = tk.Label(self.function_frame, text="次",font=("仿宋",10))
        self.Send_times_label.grid(row=0,column=2,padx=0,pady=5)  

        self.Interval_times_label = tk.Label(self.function_frame, text="间隔",font=("仿宋",10))
        self.Interval_times_label.grid(row=0,column=3,padx=5,pady=5)   

        self.Interval_times_entry = tk.Entry(self.function_frame,width=7)
        self.Interval_times_entry.grid(row=0, column=4, padx=0, pady=5, sticky="w")
        self.Interval_times_entry.insert(0,"1000")
        #ms
        self.Interval_ms_label = tk.Label(self.function_frame, text="ms",font=("仿宋",10))
        self.Interval_ms_label.grid(row=0,column=5,padx=5,pady=5) 
        #每次多少张
        self.Sheet_num_entry = tk.Entry(self.function_frame,width=6)
        self.Sheet_num_entry.grid(row=0, column=6, padx=0, pady=5, sticky="w")
        self.Sheet_num_entry.insert(0,"1")
        #张/次
        self.Sheet_num_label = tk.Label(self.function_frame, text="次",font=("仿宋",10))
        self.Sheet_num_label.grid(row=0,column=7,padx=5,pady=5) 
        #添加编号
        self.Serial_num = tk.BooleanVar()
        self.Serial_num.set(False)
        Serial_num_check = tk.Checkbutton(self.function_frame, 
                                         text="添加编号",
                                         variable=self.Serial_num,
                                         onvalue=True,
                                         offvalue=False,
                                         command=self.Add_SerialNum,
                                         font=("仿宋",10))
        Serial_num_check.grid(row=1, column=0, padx=5, pady=5, sticky="w") 

        self.Start_SerialNum_label = tk.Label(self.function_frame, text="开始编号：",font=("仿宋",10))
        self.Start_SerialNum_label.place(x=100,y=38)   

        self.Start_SerialNum_entry = tk.Entry(self.function_frame,width=7)
        self.Start_SerialNum_entry.place(x=170,y=38) 
        self.Start_SerialNum_entry.insert(0,"1")

        # 是否有图片标志位
        self.image_Flag = False
        # 加载图片
        self.Send_image_path = os.getcwd() + r"\Data\Image\send.png"
        self.Send_image2_path = os.getcwd() + r"\Data\Image\send2.png" 
        self.Stop_image_path = os.getcwd() + r"\Data\Image\stop.png"
        self.Stop_image2_path = os.getcwd() + r"\Data\Image\stop2.png"

        if not os.path.exists(self.Send_image_path) :
            log = "没有找到图片1的路径:{}".format(self.Send_image_path)
            log_message(log,logging.ERROR)
            self.Send_Data_button = tk.Button(self.function_frame,text="发送",width=10,height=2,command=self.Send_TextData,font=("仿宋",11,"bold")) 
        elif not os.path.exists(self.Send_image2_path) :
            log = "没有找到图片1的路径:{}".format(self.Send_image2_path)
            log_message(log,logging.ERROR)
            self.Send_Data_button = tk.Button(self.function_frame,text="发送",width=10,height=2,command=self.Send_TextData,font=("仿宋",11,"bold")) 
        else : 
            # 加载并调整图片大小
            logging.getLogger('PIL').setLevel(logging.WARNING)
            original_img1 = Image.open(self.Send_image_path)
            original_img2 = Image.open(self.Send_image2_path)
            original_img3 = Image.open(self.Stop_image_path)
            original_img4 = Image.open(self.Stop_image2_path)            
            # 设置目标宽高
            target_size = (100, 40)  #宽20，高10
            # 调整图片大小
            self.img1 = ImageTk.PhotoImage(original_img1.resize(target_size))
            self.img2 = ImageTk.PhotoImage(original_img2.resize(target_size))  
            self.img3 = ImageTk.PhotoImage(original_img3.resize(target_size))
            self.img4 = ImageTk.PhotoImage(original_img4.resize(target_size))  

            self.Send_Data_button = tk.Button(self.function_frame,image=self.img1, borderwidth=0,highlightthickness=0,command=self.Send_TextData)
            
            # 绑定事件
            self.Send_Data_button.bind("<Enter>", self.on_enter_imag)
            self.Send_Data_button.bind("<Leave>", self.on_leave_imag)
            self.image_Flag = True
        self.Send_Data_button.place(x=5,y=65)  # 使用 place 布局 
        # 在初始化时调用,有些要置灰
        self.Loop_send()  
        self.Add_SerialNum()
        # 快捷测试功能
        quick_test_frame = ttk.LabelFrame(self.frame, text="快捷测试功能区")
        quick_test_frame.place(x=400,y=0,width=300,height=500)


        #自测页
        self.Self_testbutton = tk.Button(quick_test_frame, text="自测页",width=8,command=self.PrintSelf_test,font=("仿宋",10,"bold"))
        self.Self_testbutton.grid(row=0,column=0,padx=(5,5),pady=(1,2))
        #半切
        self.Half_cut = tk.Button(quick_test_frame, text="半切",width=8,command=self.HalfCut_test,font=("仿宋",10,"bold"))
        self.Half_cut.grid(row=0,column=1,padx=(5,5),pady=(1,2))      
        #全切
        self.Full_cut = tk.Button(quick_test_frame, text="全切",width=8,command=self.FullCut_test,font=("仿宋",10,"bold"))
        self.Full_cut.grid(row=0,column=2,padx=(5,5),pady=(1,2))   
        #钱箱1
        self.Cash_box = tk.Button(quick_test_frame, text="钱箱1",width=8,command=self.CashBox_test,font=("仿宋",10,"bold"))
        self.Cash_box.grid(row=1,column=0,padx=(5,5),pady=(1,2))   
        #查找黑标
        self.Find_blacklabel = tk.Button(quick_test_frame, text="查找黑标",width=8,command=self.FindBlackLabel_test,font=("仿宋",10,"bold"))
        self.Find_blacklabel.grid(row=1,column=1,padx=(5,5),pady=(1,2))  
        #查找黑标2
        self.Find_blacklabelCut = tk.Button(quick_test_frame, text="黑标/切纸",width=10,command=self.FindBlackLabelCut_test,font=("仿宋",10,"bold"))
        self.Find_blacklabelCut.grid(row=1,column=2,padx=(5,5),pady=(1,2)) 
        #钱箱2
        self.Cash_box2 = tk.Button(quick_test_frame, text="钱箱2",width=8,command=self.CashBox2_test,font=("仿宋",10,"bold"))
        self.Cash_box2.grid(row=2,column=0,padx=(5,5),pady=(1,2))   
        #查找缝标
        self.Find_sewlabel = tk.Button(quick_test_frame, text="查找缝标",width=8,command=self.FindSewLabel_test,font=("仿宋",10,"bold"))
        self.Find_sewlabel.grid(row=2,column=1,padx=(5,5),pady=(1,2))  
        #查找缝标2
        self.Find_sewlabelCut = tk.Button(quick_test_frame, text="缝标/切纸",width=10,command=self.FindSewLabelCut_test,font=("仿宋",10,"bold"))
        self.Find_sewlabelCut.grid(row=2,column=2,padx=(5,5),pady=(1,2)) 

        #小票打印58mm
        Recepict58mm_frame = ttk.LabelFrame(self.frame, text="58mm:")
        Recepict58mm_frame.place(x=400,y=100,width=300,height=50)  
        self.Receipt_58mmPrn = tk.Button(Recepict58mm_frame, text="英文",width=8,command=lambda:self.Receipt_58mm(1),font=("仿宋",10,"bold"))
        self.Receipt_58mmPrn.grid(row=0,column=0,padx=(5,5),pady=(1,2))       
        self.Receipt_58mmPrn2 = tk.Button(Recepict58mm_frame, text="中文/繁体",width=10,command=lambda:self.Receipt_58mm(2),font=("仿宋",10,"bold"))
        self.Receipt_58mmPrn2.grid(row=0,column=1,padx=(5,5),pady=(1,2))  
        self.Receipt_58mmPrn3 = tk.Button(Recepict58mm_frame, text="韩文/日文",width=10,command=lambda:self.Receipt_58mm(3),font=("仿宋",10,"bold"))
        self.Receipt_58mmPrn3.grid(row=0,column=2,padx=(5,5),pady=(1,2))  
        #小票打印80mm
        Recepict80mm_frame = ttk.LabelFrame(self.frame, text="80mm:")
        Recepict80mm_frame.place(x=400,y=150,width=300,height=50)  
        self.Receipt_80mmPrn = tk.Button(Recepict80mm_frame, text="英文",width=8,command=lambda:self.Receipt_80mm(1),font=("仿宋",10,"bold"))
        self.Receipt_80mmPrn.grid(row=0,column=0,padx=(5,5),pady=(1,2))       
        self.Receipt_80mmPrn2 = tk.Button(Recepict80mm_frame, text="中文/繁体",width=10,command=lambda:self.Receipt_80mm(2),font=("仿宋",10,"bold"))
        self.Receipt_80mmPrn2.grid(row=0,column=1,padx=(5,5),pady=(1,2))  
        self.Receipt_80mmPrn3 = tk.Button(Recepict80mm_frame, text="韩文/日文",width=10,command=lambda:self.Receipt_80mm(3),font=("仿宋",10,"bold"))
        self.Receipt_80mmPrn3.grid(row=0,column=2,padx=(5,5),pady=(1,2))  
        #条形码
        Barcode_frame = ttk.LabelFrame(self.frame, text="条形码:")
        Barcode_frame.place(x=400,y=200,width=300,height=105)   

        self.BarcodeData_label = tk.Label(Barcode_frame, text="数据:",font=("仿宋",10))
        self.BarcodeData_label.grid(row=0,column=0,padx=1,pady=(1,5))
        self.BarcodeData_entry = tk.Entry(Barcode_frame, width=14)
        self.BarcodeData_entry.grid(row=0,column=1,padx=1,pady=(1,5))
        self.BarcodeData_entry.insert(0,"123456789012")

        self.BarcodePrn_button = tk.Button(Barcode_frame, text="打印",width=8,command=self.Barcode_Prn,font=("仿宋",12,"bold"))
        self.BarcodePrn_button.grid(row=0,column=3,padx=(1,3),pady=1,sticky='w')

        self.BarcodeType_label = tk.Label(Barcode_frame, text="类型:",font=("仿宋",10))
        self.BarcodeType_label.grid(row=1,column=0,padx=1,pady=1, sticky="w") 
        self.BarcodeType_enrty = ttk.Combobox(Barcode_frame, width=8, values=['UPC_A','UPC_E','ENA 13','ENA 8','CODE 39','ITF','CODEBAR',
                                                                              'CODE 93','CODE 128'])  # 根据实际情况修改串口号列表
        self.BarcodeType_enrty.grid(row=1,column=1,padx=(1,3),pady=1, sticky="w")
        self.BarcodeType_enrty.set('UPC_A')
        self.BarcodeType_enrty.bind("<<ComboboxSelected>>",self.on_barcode_type_change)

        self.BarcodeWidth_label = tk.Label(Barcode_frame, text="宽度:",font=("仿宋",10))
        self.BarcodeWidth_label.grid(row=1,column=2,padx=1,pady=1, sticky="w") 
        self.BarcodeWitdth_enrty = ttk.Combobox(Barcode_frame, width=8, values=['2','3','4','5','6'])  # 根据实际情况修改串口号列表
        self.BarcodeWitdth_enrty.grid(row=1,column=3,padx=(1,3),pady=1, sticky="w")    
        self.BarcodeWitdth_enrty.set('3')

        self.BarcodeHigh_label = tk.Label(Barcode_frame, text="高度:",font=("仿宋",10))
        self.BarcodeHigh_label.grid(row=2,column=0,padx=1,pady=1, sticky="w") 
        self.BarcodeHigh_enrty = ttk.Combobox(Barcode_frame, width=8, values=['24点','48点','72点','96点','120点','144点','168点','192点'])  # 根据实际情况修改串口号列表
        self.BarcodeHigh_enrty.grid(row=2,column=1,padx=(1,3),pady=1, sticky="w")    
        self.BarcodeHigh_enrty.set('96点')  

        self.FontLocation_label = tk.Label(Barcode_frame, text="字体:",font=("仿宋",10))
        self.FontLocation_label.grid(row=2,column=2,padx=1,pady=1, sticky="w") 
        self.FontLocation_enrty = ttk.Combobox(Barcode_frame, width=8, values=['不显示','条码上方','条码下方','条码上方和下方'])  # 根据实际情况修改串口号列表
        self.FontLocation_enrty.grid(row=2,column=3,padx=(1,3),pady=1, sticky="w")    
        self.FontLocation_enrty.set('条码下方')    

        #二维码
        QRCode_frame = ttk.LabelFrame(self.frame, text="二维码:")
        QRCode_frame.place(x=400,y=305,width=300,height=100)  

        self.QRCodeData_label = tk.Label(QRCode_frame, text="数据:",font=("仿宋",10))
        self.QRCodeData_label.grid(row=0,column=0,padx=1,pady=(1,4))
        self.QRCodeData_entry = tk.Entry(QRCode_frame, width=14)
        self.QRCodeData_entry.grid(row=0,column=1,padx=1,pady=(1,4))
        self.QRCodeData_entry.insert(0,"Hello World")

        self.QRCodePrn_button = tk.Button(QRCode_frame, text="打印",width=8,command=self.Qrcode_Prn,font=("仿宋",12,"bold"))
        self.QRCodePrn_button.grid(row=0,column=3,padx=(1,3),pady=1,sticky='w')

        self.QRCodeType_label = tk.Label(QRCode_frame, text="类型:",font=("仿宋",10))
        self.QRCodeType_label.grid(row=1,column=0,padx=1,pady=1, sticky="w") 
        self.QRCodeType_enrty = ttk.Combobox(QRCode_frame, width=8, values=['QRCODE','PD417'])  # 根据实际情况修改串口号列表
        self.QRCodeType_enrty.grid(row=1,column=1,padx=(1,3),pady=1, sticky="w")
        self.QRCodeType_enrty.set('QRCODE')

        self.QRcodeWidth_label = tk.Label(QRCode_frame, text="宽度:",font=("仿宋",10))
        self.QRcodeWidth_label.grid(row=1,column=2,padx=1,pady=1, sticky="w") 
        self.QRcodeWitdth_enrty = ttk.Combobox(QRCode_frame, width=8, values=['2','3','4','5','6'])  # 根据实际情况修改串口号列表
        self.QRcodeWitdth_enrty.grid(row=1,column=3,padx=(1,3),pady=1, sticky="w")    
        self.QRcodeWitdth_enrty.set('2')

        self.QRcodelevel_label = tk.Label(QRCode_frame, text="纠错:",font=("仿宋",10))
        self.QRcodelevel_label.grid(row=2,column=0,padx=1,pady=1, sticky="w") 
        self.QRcodelevel_enrty = ttk.Combobox(QRCode_frame, width=8, values=['纠错等级1','纠错等级2','纠错等级3','纠错等级4'])  # 根据实际情况修改串口号列表
        self.QRcodelevel_enrty.grid(row=2,column=1,padx=(1,3),pady=1, sticky="w")    
        self.QRcodelevel_enrty.set('纠错等级4')  

        self.QRcodeSize_label = tk.Label(QRCode_frame, text="大小:",font=("仿宋",10))
        self.QRcodeSize_label.grid(row=2,column=2,padx=1,pady=1, sticky="w") 
        self.QRcodeSize_enrty = ttk.Combobox(QRCode_frame, width=8, values=['1','2','3','4','5','6','7','8','9','10','11','12',
                                                                             '13','14','15','16'])  # 根据实际情况修改串口号列表
        self.QRcodeSize_enrty.grid(row=2,column=3,padx=(1,3),pady=1, sticky="w")    
        self.QRcodeSize_enrty.set('6')   
        #图片
        self.Image_label = tk.Label(self.frame, text="图片路径:",font=("仿宋",10))
        self.Image_label.place(x=400,y=410)

        self.Image_entry = tk.Entry(self.frame, width=14)
        self.Image_entry.place(x=480,y=410)
        self.Image_entry.insert(0,self.Image_DefaultPath)

        self.OpenFile_button = tk.Button(self.frame, text="打开",width=8,command=self.Open_ImagePath,font=("仿宋",10,"bold"))
        self.OpenFile_button.place(x=600,y=410)

        self.ImageSize_label = tk.Label(self.frame, text="图片大小:",font=("仿宋",10))
        self.ImageSize_label.place(x=400,y=440)

        self.ImageSize_entry = ttk.Combobox(self.frame, width=8, values=['192','384','576','832'])
        self.ImageSize_entry.place(x=480,y=440)
        self.ImageSize_entry.set('384')

        self.ImagePrn_button = tk.Button(self.frame, text="打印",width=8,command=self.Image_Prn,font=("仿宋",10,"bold"))
        self.ImagePrn_button.place(x=600,y=440)

    #移动到图片
    def on_enter_imag(self,event):
        if self.stop_flag:
            self.Send_Data_button.config(image=self.img4)
        else :
            self.Send_Data_button.config(image=self.img2)

    #离开图片
    def on_leave_imag(self,event):
        if self.stop_flag:
            self.Send_Data_button.config(image=self.img3)
        else :
            self.Send_Data_button.config(image=self.img1)

    def on_barcode_type_change(self, event):
        """
        条形码的数据的初始值与条形码的类型做一个绑定
        """
        barcode_defaults = {
            'UPC_A': "123456789012",
            'UPC_E': "023456000078",
            'ENA 13': "023456000089",
            'ENA 8': "02345600",
            'CODE 39': "02345601",
            'ITF' : "02345602",
            'CODEBAR' : "234560",
            'CODE 93' : "*234560*",
            'CODE 128' : "*234560*",
        }
        barcode_type = self.BarcodeType_enrty.get()
        default_value = barcode_defaults.get(barcode_type, "")
        self.BarcodeData_entry.delete(0, tk.END)
        self.BarcodeData_entry.insert(0, default_value)

    def Image_Prn(self):
        FilePath = self.Image_entry.get()
        image_size = int(self.ImageSize_entry.get())
        ret = queue_handler.Print_Image(FilePath,image_size)
    def Open_ImagePath(self):
        FilePath = filedialog.askopenfilename(title="选择图片路径",filetypes=[("Image Files","*.png;*.jpg;*.jpeg;*.bmp;")])
        if FilePath:
            self.Image_entry.delete(0,tk.END)
            self.Image_entry.insert(0,FilePath)

    def Qrcode_Prn(self):
        QrCodeData = self.QRCodeData_entry.get()
        QrCodeWidth = self.QRcodeWitdth_enrty.get()
        Qrcodelevel = self.QRcodelevel_enrty.get()
        QrcodeSize = self.QRcodeSize_enrty.get()
        #纠错等级
        Qrcodelevels = {
            '纠错等级1': "1",
            '纠错等级2': "2",
            '纠错等级3': "3",
            '纠错等级4': "4",
        }
        QrCode_Init = "1d 77 "
        QrCode_width = QrCodeWidth.zfill(2) +  " "
        QrCode_PrintDat = "1D 6B 61 "
        QrCode_Size = int(QrcodeSize) 
        QrCode_Size = hex(QrCode_Size) 
        QrCode_Size = QrCode_Size.upper()[2:].zfill(2) +  " "
        Codelevel = Qrcodelevels.get(Qrcodelevel, "2")
        Qrcode_level = Codelevel.zfill(2) + " "

        little_endian_bytes = struct.pack('<H', len(QrCodeData))  # '<H' 表示小端格式的无符号短整数
        Qrcode_lenhex = little_endian_bytes.hex().upper()  # 转换为16进制字符串并转为大写
        formatted_str = ' '.join([Qrcode_lenhex[i:i+2] for i in range(0, len(Qrcode_lenhex), 2)])
        Qrcode_Datlen = formatted_str + " "
        Qrcode_data = QrCodeData.encode('utf-8') 
        Qrcode_data_hex =  ' '.join(format(byte, '02x') for byte in Qrcode_data)

        Send_pack = QrCode_Init+QrCode_width+QrCode_PrintDat+QrCode_Size+Qrcode_level+Qrcode_Datlen+Qrcode_data_hex
        Qrcode_bytes_Data = bytes.fromhex(Send_pack)
        queue_handler.Print_QRCode(QrCodeData,int(QrCodeWidth),int(QrcodeSize),int(Codelevel),Qrcode_bytes_Data)

    def Barcode_Prn(self):
        #条形码的宽度
        barcode_widths = {
            '2': "1d 77 02 ",
            '3': "1d 77 03 ",
            '4': "1d 77 04 ",
            '5': "1d 77 05 ",
            '6': "1d 77 06 ",
        }
        #条形码的高度
        barcode_highs = {
            '24点': "1d 68 18 ",
            '48点': "1d 68 30 ",
            '72点': "1d 68 48 ",
            '96点': "1d 68 60 ",
            '120点': "1d 68 78 ",
            '144点': "1d 68 90 ",
            '168点': "1d 68 A8 ",
            '192点': "1d 68 C0 ",
        }
        #字体位置
        barcode_location = {
            '不显示': "1d 48 00 ",
            '条码上方': "1d 48 01 ",
            '条码下方': "1d 48 02 ",
            '条码上方和下方': "1d 48 03 ",           
        }
        #条码类型
        barcode_types = {
            'UPC_A': "1d 6b 41 ",
            'UPC_E': "1d 6b 42 ",
            'ENA 13': "1d 6b 43 ",
            'ENA 8': "1d 6b 44 ",
            'CODE 39': "1d 6b 45 ",
            'ITF' : "1d 6b 46 ",
            'CODEBAR' : "1d 6b 47 ",
            'CODE 93' : "1d 6b 48 ",
            'CODE 128' : "1d 6b 49 ",
        }      
        #Barcode Tol Value
        Barcode_Init = "1b 61 00 1b 24 00 00 "
        #初始值
        Barcode_Total = Barcode_Init
        #宽度
        Temp = barcode_widths.get(self.BarcodeWitdth_enrty.get(), "")
        Barcode_Total = Barcode_Total + Temp
        #高度
        Temp = barcode_highs.get(self.BarcodeHigh_enrty.get(), "")
        Barcode_Total = Barcode_Total + Temp
        #字体位置
        Temp = barcode_location.get(self.FontLocation_enrty.get(), "")
        Barcode_Total = Barcode_Total + Temp   
        #barcode 类型
        Temp = barcode_types.get(self.BarcodeType_enrty.get(), "")
        Barcode_Total = Barcode_Total + Temp    
        #数据长度
        data = self.BarcodeData_entry.get() 
        data_length = len(data)
        Temp = format(data_length, '02X')  # 转换为16进制并补齐两位
        Barcode_Total = Barcode_Total + Temp + " "
        #数据
        Temp = " ".join(f'{ord(x):02x}' for x in data)
        Barcode_Total = Barcode_Total + Temp
        #转成16进制写入队列
        Bar_byte_data = bytes.fromhex(Barcode_Total)
        queue_handler.write_to_queue(Bar_byte_data,"打印条形码")    

    def Receipt_80mm(self,language):
        if not os.path.exists(self.DataPath_80mm):
            log = "没有找到小票数据路径; 当前路径:{}".format(self.DataPath_80mm)
            log_message(log,logging.ERROR)
            return 
        with open(self.DataPath_80mm, 'r') as file:
            content = file.read()
        if language == 1:
            match = re.search(r'"English_Receipt":"([^"]+)"', content)
        elif language == 2:
            match = re.search(r'"Chinese_Receipt":"([^"]+)"', content)
        elif language == 3:
            match = re.search(r'"Japan_Receipt":"([^"]+)"', content)
        else :
            log = "没有存储要打印的小票字段 :{}".format(language)
            log_message(log,logging.ERROR)      
            return      
        if match:
            Rcontent = match.group(1)
            byte_data = bytes.fromhex(Rcontent)
            if language == 1:
                queue_handler.write_to_queue(byte_data,"英文80mm票据")
            elif language == 2:
                queue_handler.write_to_queue(byte_data,"中文简体/繁体80mm票据")
            elif language == 3:
                queue_handler.write_to_queue(byte_data,"韩文/日文80mm票据")
            else :
               log_message("不是打印的票据",logging.ERROR)  
        else:
            log_message("没有找到小票字段",logging.ERROR) 


    def Receipt_58mm(self,language=1):
        if not os.path.exists(self.DataPath_58mm):
            log = "没有找到小票数据路径; 当前路径:{}".format(self.DataPath_58mm)
            log_message(log,logging.ERROR)
            return 
        with open(self.DataPath_58mm, 'r') as file:
            content = file.read()
        if language == 1:
            match = re.search(r'"English_Receipt":"([^"]+)"', content)
        elif language == 2:
            match = re.search(r'"Chinese_Receipt":"([^"]+)"', content)
        elif language == 3:
            match = re.search(r'"Japan_Receipt":"([^"]+)"', content)
        else :
            log = "没有存储要打印的小票字段 :{}".format(language)
            log_message(log,logging.ERROR)      
            return      
        if match:
            Rcontent = match.group(1)
            byte_data = bytes.fromhex(Rcontent)
            if language == 1:
                queue_handler.write_to_queue(byte_data,"英文58mm票据")
            elif language == 2:
                queue_handler.write_to_queue(byte_data,"中文简体/繁体58mm票据")
            elif language == 3:
                queue_handler.write_to_queue(byte_data,"韩文/日文58mm票据")
            else :
               log_message("不是打印的票据",logging.ERROR)  
        else:
            log_message("没有找到小票字段",logging.ERROR) 
    #查找缝标并切纸
    def FindSewLabelCut_test(self):
        byte_data = bytes.fromhex("0e 1b 69")
        queue_handler.write_to_queue(byte_data,"查找缝标并切纸")
    #查找缝标
    def FindSewLabel_test(self):
        byte_data = bytes.fromhex("0e")
        queue_handler.write_to_queue(byte_data,"查找缝标")
    #钱箱2
    def CashBox2_test(self):
        byte_data = bytes.fromhex("1b 70 01 14 3c")
        queue_handler.write_to_queue(byte_data,"钱箱2")
    #查找黑标并切纸
    def FindBlackLabelCut_test(self):
        byte_data = bytes.fromhex("0c 1b 69")
        queue_handler.write_to_queue(byte_data,"查找黑标并切纸")
    #查找黑标
    def FindBlackLabel_test(self):
        byte_data = bytes.fromhex("0c")
        queue_handler.write_to_queue(byte_data,"查找黑标")
    #钱箱1
    def CashBox_test(self):
        byte_data = bytes.fromhex("1b 70 00 14 3c")
        queue_handler.write_to_queue(byte_data,"钱箱1")
    #全切刀
    def FullCut_test(self):
        byte_data = bytes.fromhex("1b 69")
        queue_handler.write_to_queue(byte_data,"全切刀")
    #半切刀
    def HalfCut_test(self):
        byte_data = bytes.fromhex("1b 6d")
        queue_handler.write_to_queue(byte_data,"半切刀")
    #打印自测页
    def PrintSelf_test(self):
        byte_data = bytes.fromhex("1b 40 12 54")
        queue_handler.write_to_queue(byte_data,"打印自测页")

    def MonitorStatus(self):
        """
        打印机状态监控
        """
        Status_window = tk.Toplevel(self.frame)
        Status_window.title("状态监测")
        # 移除最小化和最大化按钮，只保留关闭按钮
        Status_window.attributes('-toolwindow', True)      

        # 锁定父窗口
        Status_window.grab_set()
        x, y = self.parent.winfo_pointerxy()  # 获取鼠标的x和y坐标
        Status_window.geometry(f"300x220+{x}+{y-200}")
        # 在 Toplevel 窗口中创建一个 Frame
        frame = tk.Frame(Status_window, bg='lightgray')
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    

        #纸将尽
        self.PaperFinal_canvas ,self.PaperFinal_rect_id = self.Creat_Statu_check(frame,0,"纸将尽侦测")       
        #打印机堵纸
        self.PaperJam_canvas ,self.PaperJam_rect_id = self.Creat_Statu_check(frame,1,"打印机堵纸")   
        #机芯未连接
        self.MoveDisconnect_canvas ,self.MoveDisconnect_rect_id = self.Creat_Statu_check(frame,2,"机芯未连接")  
        #打印机缺纸
        self.LackPaper_canvas ,self.LackPaper_rect_id = self.Creat_Statu_check(frame,3,"打印机缺纸")  
        #切刀错误
        self.CutError_canvas ,self.CutError_rect_id = self.Creat_Statu_check(frame,4,"切刀错误")  
        #打印机过热
        self.tempHigh_canvas ,self.tempHigh_rect_id = self.Creat_Statu_check(frame,5,"温度过高")
        #轴未压下
        self.OpenLid_canvas ,self.OpenLid_rect_id = self.Creat_Statu_check(frame,6,"轴未压下")
        #定位错误
        self.FixError_canvas  ,self.FixError_rect_id = self.Creat_Statu_check(frame,7,"定位错误")

        self.PrinterIdEntry = []
        #固件版本
        self.PrinterIdEntry.append(self.Creat_PrintID_check(frame,0,"固件版本:"))
        #制造商
        self.PrinterIdEntry.append(self.Creat_PrintID_check(frame,1,"制造商:"))
        #打印机名称
        self.PrinterIdEntry.append(self.Creat_PrintID_check(frame,2,"打印机名称:"))   
        #打印机名称
        self.PrinterIdEntry.append(self.Creat_PrintID_check(frame,3,"ID:"))   
        #编码方式
        self.PrinterIdEntry.append(self.Creat_PrintID_check(frame,4,"编码方式:"))  
        for num in self.PrinterIdEntry:
            num.delete(0, tk.END)
        #循环检测
        self.Loopcheck_button = tk.Button(frame, text="循环检测",width=8,command=lambda:self.Printer_Status_check(0),font=("仿宋",10,"bold"),bg="green")
        self.Loopcheck_button.place(x=100,y=140)   
        #手动检测
        self.handcheck_button = tk.Button(frame, text="手动检测",width=8,command=lambda:self.Printer_Status_check(1),font=("仿宋",10,"bold"),bg="white")
        self.handcheck_button.place(x=180,y=140)    
        #打印机ID查询
        self.PrinterId_button = tk.Button(frame, text="打印机ID查询",width=12,command=lambda:self.Printer_Status_check(2),font=("仿宋",10,"bold"),bg="white")
        self.PrinterId_button.place(x=130,y=170)    
        # 启动周期性检查函数
        self.check_status_periodically(Status_window)
        # 阻塞直到窗口关闭
        Status_window.wait_window(Status_window)
        
    # 修改颜色的函数
    def change_rectangle_color(self,canvas,rect_id, new_color):
        canvas.itemconfig(rect_id, fill=new_color)

    def check_status_periodically(self, window):
        count = 0
        byte_data = [0x00,0x00,0x00,0x00]
        if self.receiveStatus_array:  # 检查列表是否有数据
            for hex_string in self.receiveStatus_array:
                # 将十六进制字符串转换为字节
                byte_data[count] =int(hex_string, 16)
                count += 1
            #上盖开
            if byte_data[1] & 0x04:
                self.change_rectangle_color(self.OpenLid_canvas,self.OpenLid_rect_id, "red")
            else :
                self.change_rectangle_color(self.OpenLid_canvas,self.OpenLid_rect_id, "green")
            #打印机缺纸 
            if byte_data[1] & 0x20:
                self.change_rectangle_color(self.LackPaper_canvas,self.LackPaper_rect_id, "red")
            else :
                self.change_rectangle_color(self.LackPaper_canvas,self.LackPaper_rect_id, "green")
            #切刀错误
            if byte_data[2] & 0x08:
                self.change_rectangle_color(self.CutError_canvas,self.CutError_rect_id, "red")
            else :
                self.change_rectangle_color(self.CutError_canvas,self.CutError_rect_id, "green")
            #打印机温度过高
            if byte_data[2] & 0x40:
                self.change_rectangle_color(self.tempHigh_canvas,self.tempHigh_rect_id, "red")
            else :
                self.change_rectangle_color(self.tempHigh_canvas,self.tempHigh_rect_id, "green")
            #纸将尽
            if byte_data[3] & 0x0C or byte_data[3] & 0x60:
                self.change_rectangle_color(self.PaperFinal_canvas,self.PaperFinal_rect_id, "red")
            else :
                self.change_rectangle_color(self.PaperFinal_canvas,self.PaperFinal_rect_id, "green")

        if self.receiveId_array:
            ReceiveId_Array = self.receiveId_array
            for hex_string in ReceiveId_Array:
                # 将十六进制字符串转换为字节
                byte_data = bytes.fromhex(hex_string)
                # 转换为字符串
                string_data = byte_data.decode('utf-8', errors='ignore')  # 使用 'ignore' 来避免解码错误
                self.PrinterIdEntry[count].delete(0, tk.END)
                self.PrinterIdEntry[count].insert(0,string_data)
                count+=1

            if len(self.receiveId_array) >= 5:
                self.receiveId_array.clear()     
                self.MonitorIDFlag = False   

        window.after(1000, self.check_status_periodically, window)

    def Send_StatusCheck(self,mode):
        if mode == 0:
            self.receiveStatus_array.clear()
            byte_data = bytes.fromhex("10 04 01")
            queue_handler.write_to_queue(byte_data,"打印机状态查询1")
            byte_data = bytes.fromhex("10 04 02")
            queue_handler.write_to_queue(byte_data,"打印机状态查询2")
            byte_data = bytes.fromhex("10 04 03")
            queue_handler.write_to_queue(byte_data,"打印机状态查询3")
            byte_data = bytes.fromhex("10 04 04")
            queue_handler.write_to_queue(byte_data,"打印机状态查询4")
        elif mode == 1:
            self.receiveStatus_array.clear()
            self.receiveId_array.clear()
            byte_data = bytes.fromhex("1D 49 41")
            queue_handler.write_to_queue(byte_data,"打印机ID查询1")
            byte_data = bytes.fromhex("1D 49 42")
            queue_handler.write_to_queue(byte_data,"打印机ID查询2")
            byte_data = bytes.fromhex("1D 49 43")
            queue_handler.write_to_queue(byte_data,"打印机ID查询3")
            byte_data = bytes.fromhex("1D 49 44")
            queue_handler.write_to_queue(byte_data,"打印机ID查询4")
            byte_data = bytes.fromhex("1D 49 45")
            queue_handler.write_to_queue(byte_data,"打印机ID查询5")

    def Printer_Status_check(self,mode=0):
        if self.MonitorFlag==False:
            self.MonitorFlag = True
            self.MonitorIDFlag = False
        if mode == 0:
            self.Loopcheck_button.config(bg="green")  # 修改颜色
            self.handcheck_button.config(bg="white")  # 修改颜色
            self.PrinterId_button.config(bg="white")
            self.Send_StatusCheck(0)
        elif mode == 1:
            self.Loopcheck_button.config(bg="white")  # 修改颜色
            self.handcheck_button.config(bg="green")  # 修改颜色
            self.PrinterId_button.config(bg="white")
            self.Send_StatusCheck(0)
        else :
            self.Loopcheck_button.config(bg="white")  # 修改颜色
            self.handcheck_button.config(bg="white")  # 修改颜色
            self.PrinterId_button.config(bg="green")  # 修改颜色
            self.MonitorFlag = False
            self.MonitorIDFlag = True
            self.Send_StatusCheck(1)

    def Creat_Statu_check(self,frame, _row, _text, initial_color="green"):
        canvas = tk.Canvas(frame, width=10, height=10, bg='lightgray', highlightthickness=1, highlightbackground='black')
        rect_id = canvas.create_rectangle(0, 0, 10, 10, fill=initial_color)  # 初始颜色为绿色
        canvas.grid(row=_row, column=0, padx=5, pady=(1,0),sticky="w")

        label = tk.Label(frame, text=_text, bg='lightgray')
        label.grid(row=_row, column=1, padx=5, pady=(1,0),sticky="w")    
        return canvas ,rect_id
    
    def Creat_PrintID_check(self,frame, _row, _text):
        label = tk.Label(frame, text=_text, bg='lightgray')
        label.grid(row=_row, column=2, padx=5, pady=(1,0),sticky="w")   

        entry = tk.Entry(frame, width=13)
        entry.grid(row=_row, column=3, padx=1, pady=2,sticky="w")
        return entry
    
    def Loop_Send_Fun(self):
        Send_times = self.Send_times_entry.get()
        Delay_time = int(self.Interval_times_entry.get())
        #添加编码
        Number_Flag = self.Serial_num.get()
        #编码开始号码
        Start_Number = self.Start_SerialNum_entry.get()

        if self.SentTimes >= int(Send_times):
            self.stop_flag = False

        if self.stop_flag:
            self.SentTimes+=1
            log = "循环发送" + str(self.SentTimes) + "/" + Send_times
            self.Sheet_num_entry.delete(0,tk.END)
            self.Sheet_num_entry.insert(0,str(self.SentTimes))
            queue_handler.write_to_queue(self.Temp_data,log) 
            self.frame.after(Delay_time, self.Loop_Send_Fun)
        else :
            self.Loop_send()
            if self.image_Flag:
                self.Send_Data_button.config(image=self.img2)
            else :
                self.Send_Data_button.config(text="发送")       
    def Send_TextData(self):
        # 获取文本框的数据
        loop_flag = self.Send_loop.get()
        Delay_time = int(self.Interval_times_entry.get())
        if self.stop_flag == True:
            self.stop_flag = False
            self.Loop_Send_Fun()
            return 
        text_data = self.send_text.get("1.0", tk.END)  # 从第一行第一列到最后
        hex_flag = self.Hex_send_flag.get()
        hex_data = re.findall(r'[0-9A-Fa-f]+', text_data)
        new_hex_data = [item for item in hex_data if len(item) > 1]
        # 将过滤后的数据合并为一个字符串
        filtered_text = ''.join(new_hex_data)
        if hex_flag :
            try :
                byte_data = bytes.fromhex(filtered_text)
                queue_handler.write_to_queue(byte_data,"发送文本框数据(16进制)")   
                self.Temp_data = byte_data
            except ValueError as e:
                messagebox.showerror("错误", f"文本框数据有错\n错误信息: {e}")
                return 
        else :
             queue_handler.write_to_queue(text_data,"发送文本框数据(非16进制)")    
             self.Temp_data = text_data
        #获取发送方式
        if loop_flag == True:
            self.stop_flag = True
            self.SentTimes = 1
            self.Sheet_num_entry.delete(0,tk.END)
            self.Sheet_num_entry.insert(0,str(self.SentTimes))
            for widget in self.function_frame.winfo_children():
                widget.config(state='disabled')
            self.Send_Data_button.config(state='normal')
            self.Sheet_num_entry.config(state='normal')
            if self.image_Flag:
                self.Send_Data_button.config(image=self.img4)
            else :
                self.Send_Data_button.config(text="停止")
        if self.stop_flag:
            self.frame.after(Delay_time, self.Loop_Send_Fun)

    def Add_SerialNum(self):
        ret = self.Serial_num.get()
        if not ret :
            self.Start_SerialNum_label.config(state='disabled')
            self.Start_SerialNum_entry.config(state='disabled')
        else :
            self.Start_SerialNum_label.config(state='normal')
            self.Start_SerialNum_entry.config(state='normal')            
    def Loop_send(self):
        # 启用所有控件
        ret = self.Send_loop.get()
        if not ret :
            for widget in self.function_frame.winfo_children():
                widget.config(state='disabled')
            self.Loop_send_check.config(state='normal')
            self.Send_Data_button.config(state='normal')
        else :
            for widget in self.function_frame.winfo_children():
                widget.config(state='normal')           
            self.Add_SerialNum()

    #向接收区插入数据
    def insert_recetext(self,data):
        if self.Hex_reve_flag.get() == False:
            # 去掉空格
            hex_string = data.replace(" ", "")
            # 将十六进制字符串转换为字节
            byte_data = bytes.fromhex(hex_string)
            # 解码为普通字符串
            normal_string = byte_data.decode('utf-8')
        else :
            normal_string = data 
        self.recv_text.insert(tk.END, f"{normal_string}\n")  # 更新文本框
        self.recv_text.see(tk.END)  # 滚动到最后一行
        if self.MonitorFlag:
            self.receiveStatus_array.append(data)
        if self.MonitorIDFlag:
            self.receiveId_array.append(data)
    def Hex_model(self):
        pass
    def open_file(self):
        pass
    def send_data():
        # 处理发送数据的逻辑
        pass

if __name__ == "__main__":

    root = tk.Tk()
    app = Esc_Test(root)
    root.mainloop()