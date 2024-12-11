# print_quality_test.py
import tkinter as tk
from tkinter import ttk
import os
from APP.queue_manager import queue_handler  # 自己调用

    

class Quality_Test:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bd=2, relief=tk.GROOVE)
        self.frame.pack(fill=tk.BOTH, expand=True)
        # 只有在作为主程序运行时才设置窗口大小
        if __name__ == "__main__":
            parent.geometry("700x500+600+300")

        Current_DIR = os.getcwd()
        self._3inches_dir = os.path.join(Current_DIR, r"Data\Quality\3inches")
        self._2inches_dir = os.path.join(Current_DIR, r"Data\Quality\2inches")

        #走纸名称
        self.FeedPaper_name = r"\走纸误差测试.txt"
        self.BlankPaper_name = r"\左右余白测试.txt"
        self.Noise_Name = r"\噪音测试.txt"
        self.PrintQuality_name = r"\打印效果测试.txt"
        self.ModulePrint_name = r"\模块打印测试.txt"
        self.MaxWidth_name = r"\最大宽度测试.txt"
        self.Barcode_name = r"\条码打印测试.txt"
        self.Compress_name = r"\打印压缩测试.txt"
        self.Trailin_name = r"\打印拖尾测试.txt"
        self.DesitySet_name = r"\浓度打印测试.txt"

        #尺寸选择区域
        self.Inches_option_frame =ttk.Labelframe(self.frame,text="尺寸选择") 
        self.Inches_option_frame.place(x=0,y=5,width=700,height=50)
        self.inches_option = tk.StringVar()
        self.inches_option.set("3inches")
        self.two_inches_paper = tk.Radiobutton(self.Inches_option_frame, text="2寸", variable=self.inches_option, value="2inches")
        self.two_inches_paper.place(x=10,y=5)
        self.three_inches_paper = tk.Radiobutton(self.Inches_option_frame, text="3寸", variable=self.inches_option, value="3inches")
        self.three_inches_paper.place(x=110,y=5)
        #传动特性区 Rotational characteristics
        Rota_character_frame = ttk.Labelframe(self.frame,text="转动特性测试")
        Rota_character_frame.place(x=0,y=60,width=700,height=100)
        #累积走纸误差测试
        self.FeedTest_button = tk.Button(Rota_character_frame,text="累积走纸误差测试",width=18,command=self.feedPaperTest,font=("仿宋",12,"bold"))
        self.FeedTest_button.grid(row=0,column=0,padx=10,pady=10,sticky='w')
        #左右余白误差测试
        self.BlankTest_button = tk.Button(Rota_character_frame,text="左右余白测试",width=16,command=self.Blank_Test,font=("仿宋",12,"bold"))
        self.BlankTest_button.grid(row=0,column=1,padx=10,pady=10,sticky='w')
        #噪音测试
        self.NoiseTest_button = tk.Button(Rota_character_frame,text="噪音测试",width=12,command=self.NoiseTest,font=("仿宋",12,"bold"))
        self.NoiseTest_button.grid(row=0,column=2,padx=10,pady=10,sticky='w')

        #打印效果区

        #打印效果测试
        PrintQuality_frame = ttk.LabelFrame(self.frame,text="打印效果测试")
        PrintQuality_frame.place(x=0,y=165,width=700,height=180)
        #模块打印测试
        self.ModulePrint_button = tk.Button(PrintQuality_frame,text="模块打印测试",width=16,command=self.ModuleTest,font=("仿宋",12,"bold"))
        self.ModulePrint_button.grid(row=0,column=0,padx=10,pady=10,sticky='w')
        #最大宽度测试        
        self.MaxWidth_button = tk.Button(PrintQuality_frame,text="最大宽度测试",width=16,command=self.MaxWidthTest,font=("仿宋",12,"bold"))
        self.MaxWidth_button.grid(row=0,column=1,padx=10,pady=10,sticky='w')
        #打印效果测试        
        self.PrintQuality_button = tk.Button(PrintQuality_frame,text="打印效果测试",width=16,command=self.PrintQualityTest,font=("仿宋",12,"bold"))
        self.PrintQuality_button.grid(row=0,column=2,padx=10,pady=10,sticky='w')
        #条码打印测试
        self.BarCode_button = tk.Button(PrintQuality_frame,text="条码打印测试",width=16,command=self.BarcodePrintTest,font=("仿宋",12,"bold"))
        self.BarCode_button.grid(row=1,column=0,padx=10,pady=10,sticky='w')       
        #打印压缩测试
        self.Compress_button = tk.Button(PrintQuality_frame,text="打印压缩测试",width=16,command=self.CompressPrintTest,font=("仿宋",12,"bold"))
        self.Compress_button.grid(row=1,column=1,padx=10,pady=10,sticky='w')   
        #打印拖尾测试
        self.Trailin_button = tk.Button(PrintQuality_frame,text="打印拖尾测试",width=16,command=self.TrialingPrintTest,font=("仿宋",12,"bold"))
        self.Trailin_button.grid(row=1,column=2,padx=10,pady=10,sticky='w')   
        #8段浓度等级测试
        self.DesityTest_button = tk.Button(PrintQuality_frame,text="8段浓度打印测试",width=18,command=self.DesityPrintTest,font=("仿宋",12,"bold"))
        self.DesityTest_button.grid(row=2,column=0,padx=10,pady=10,sticky='w')
        #浓度设置
        self.DesitySet_label = tk.Label(self.frame,text="浓度设置:")
        self.DesitySet_label.place(x=0,y=350)
        self.DesitySet_entry = ttk.Combobox(self.frame, width=10,values=['1','2','3','4','5','6','7','8'])
        self.DesitySet_entry.place(x=60,y=350)
        self.DesitySet_entry.set('4')
        self.DesitySet_button = tk.Button(self.frame,text="设置",width=6,command=self.DesityPrintSet,font=("仿宋",12,"bold"))
        self.DesitySet_button.place(x=160,y=350)
        #2寸的路径
        self._2inches_path = tk.Label(self.frame,text="2寸的路径:")
        self._2inches_path.place(x=0,y=400)    
        self._2inchespath_entry = tk.Entry(self.frame, width=60)
        self._2inchespath_entry.place(x=80,y=400)
        self._2inchespath_entry.insert(0,self._2inches_dir)
        self.Open2inches_button = tk.Button(self.frame, text="打开",width=8,command=self.open_2inchesdir,font=("仿宋",10,"bold"))
        self.Open2inches_button.place(x=520,y=400) 
        self.Set2inchespath_button = tk.Button(self.frame, text="设置",width=8,command=self.set_2inchesdir,font=("仿宋",10,"bold"))
        self.Set2inchespath_button.place(x=600,y=400) 
        #3寸路径 
        self._3inches_path = tk.Label(self.frame,text="3寸的路径:")
        self._3inches_path.place(x=0,y=430)      
        self._3inchespath_entry = tk.Entry(self.frame, width=60)
        self._3inchespath_entry.place(x=80,y=430)
        self._3inchespath_entry.insert(0,self._3inches_dir)
        self.Open3inches_button = tk.Button(self.frame, text="打开",width=8,command=self.open_3inchesdir,font=("仿宋",10,"bold"))
        self.Open3inches_button.place(x=520,y=430) 
        self.Set3inchespath_button = tk.Button(self.frame, text="设置",width=8,command=self.set_3inchesdir,font=("仿宋",10,"bold"))
        self.Set3inchespath_button.place(x=600,y=430) 

        

    
    def Get_filePath(self,file_name):
        inches = self.inches_option.get()
        if inches == "2inches":
            file_path = self._2inches_dir+file_name
        elif inches == "3inches":
            file_path = self._3inches_dir+file_name
        else :
            file_path = "null"
        return file_path
    #累计走纸误差测试
    def feedPaperTest(self):
        file_path = self.Get_filePath(self.FeedPaper_name)
        if os.path.exists(file_path): 
            # 打开并读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:   
                content = file.read()
            if content:
                byte_data = bytes.fromhex(content)
                queue_handler.write_to_queue(byte_data,"累积走纸误差")

    #左右余白测试
    def Blank_Test(self):
        file_path = self.Get_filePath(self.BlankPaper_name)
        if os.path.exists(file_path): 
            # 打开并读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:   
                content = file.read()
            if content:
                byte_data = bytes.fromhex(content)
                queue_handler.write_to_queue(byte_data,"左右余白测试")
    def NoiseTest(self):
        pass
    #黑块打印测试
    def ModuleTest(self):
        file_path = self.Get_filePath(self.ModulePrint_name)
        if os.path.exists(file_path): 
            # 打开并读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:   
                content = file.read()
            if content:
                byte_data = bytes.fromhex(content)
                queue_handler.write_to_queue(byte_data,"模块打印测试")

    def MaxWidthTest(self):
        file_path = self.Get_filePath(self.MaxWidth_name)
        if os.path.exists(file_path): 
            # 打开并读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:   
                content = file.read()
            if content:
                byte_data = bytes.fromhex(content)
                queue_handler.write_to_queue(byte_data,"最大打印宽度测试")
                
    def PrintQualityTest(self):
        file_path = self.Get_filePath(self.PrintQuality_name)
        if os.path.exists(file_path): 
            # 打开并读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:   
                content = file.read()
            if content:
                byte_data = bytes.fromhex(content)
                queue_handler.write_to_queue(byte_data,"打印效果测试")
    #条码打印测试
    def BarcodePrintTest(self):
        file_path = self.Get_filePath(self.Barcode_name)
        if os.path.exists(file_path): 
            # 打开并读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:   
                content = file.read()
            if content:
                byte_data = bytes.fromhex(content)
                queue_handler.write_to_queue(byte_data,"条码打印测试")
    #打印压缩测试
    def CompressPrintTest(self):
        file_path = self.Get_filePath(self.Compress_name)
        if os.path.exists(file_path): 
            # 打开并读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:   
                content = file.read()
            if content:
                byte_data = bytes.fromhex(content)
                queue_handler.write_to_queue(byte_data,"打印压缩测试")
    #打印拖尾测试
    def TrialingPrintTest(self):
        file_path = self.Get_filePath(self.Trailin_name)
        if os.path.exists(file_path): 
            # 打开并读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:   
                content = file.read()
            if content:
                byte_data = bytes.fromhex(content)
                queue_handler.write_to_queue(byte_data,"打印拖尾测试")

    #浓度打印测试
    def DesityPrintTest(self):
        file_path = self.Get_filePath(self.DesitySet_name)
        if os.path.exists(file_path): 
            # 打开并读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:   
                content = file.read()
            if content:
                byte_data = bytes.fromhex(content)
                queue_handler.write_to_queue(byte_data,"浓度打印测试")

    def DesityPrintSet(self):
        pass
    def open_2inchesdir(self):
        pass
    def set_2inchesdir(self):
        pass
    def open_3inchesdir(self):
        pass
    def set_3inchesdir(self):
        pass       
if __name__ == "__main__":
    root = tk.Tk()
    app = Quality_Test(root)
    root.mainloop()
