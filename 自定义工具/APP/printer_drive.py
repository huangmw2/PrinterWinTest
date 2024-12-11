import tkinter as tk
from tkinter import ttk,  filedialog, messagebox
import win32print
import win32api
import win32ui
import win32com.client
import os
from PIL import Image, ImageWin

class Driver_Test:
    def __init__(self,parent):

        if __name__ == "__main__":
            self.root = parent
            self.root.title("Driver测试")
            self.root.geometry("700x500+600+300")
        self.printer_list=[]
        self.ImageDefault_path = "./test.bmp"
        self.WordDefault_path = "./text.docx"
        self.PdfDefault_path = "./test.pdf"
        self.ExcelDefault_path = "./test.xlsx"
        self.PPTDefault_path = "./test.pptx"
        self.TXTDefault_path = "./test.txt"
        #创建一个矩形区域
        self.frame = tk.Frame(parent, bd=2, relief=tk.GROOVE)
        self.frame.pack(fill='both',expand=True)
        #打印机名称显示和选择
        self.label = tk.Label(self.frame, text="打印机名称：", font=("仿宋", 12))
        self.label.place(x=5,y=10)
        self.Printer_entry = ttk.Combobox(self.frame,width=20)
        self.Printer_entry.place(x=100,y=10)
        self.printer_list = self.get_printers()
        self.Printer_entry['values'] = self.printer_list
        self.Printer_entry.set(self.printer_list[0]) #默认第一个打印机
        #一键测试
        self.OneClick_test =  tk.Button(self.frame, text="一键测试",width=8,command=self.OneClickTest,font=("仿宋",12,"bold"))
        self.OneClick_test.place(x=280,y=10)
        #取消所有队列
        self.Cancelteam_test = tk.Button(self.frame, text="取消队列",width=8,command=self.CancelTeam,font=("仿宋",12))
        self.Cancelteam_test.place(x=380,y=10)
        #暂停队列
        self.PauseTask_test = tk.Button(self.frame, text="暂停队列",width=8,command=self.PauseTask,font=("仿宋",12))
        self.PauseTask_test.place(x=480,y=10)
        #恢复队列
        self.RecoveryTask_test = tk.Button(self.frame, text="恢复队列",width=8,command=self.RecoveryTask,font=("仿宋",12))
        self.RecoveryTask_test.place(x=580,y=10)   
        #图片路径选择及设置按钮
        self.label = tk.Label(self.frame,text="图片路径:",font=("仿宋",12))
        self.label.place(x=5,y=80)
        self.ImagePath_enrty = tk.Entry(self.frame,width=50)
        self.ImagePath_enrty.place(x=90,y=80)
        self.OpenImage_button = tk.Button(self.frame, text="打开",width=6,command=self.OpenImagePath,font=("仿宋",12))
        self.OpenImage_button.place(x=460,y=80)
        self.ImageTest_button = tk.Button(self.frame, text="测试",width=6,command=self.ImagePrintTest,font=("仿宋",12))
        self.ImageTest_button.place(x=520,y=80)
        self.ImagePath_enrty.insert(0,self.ImageDefault_path)

        #doc路径选择及设置按钮
        self.label = tk.Label(self.frame,text="word路径:",font=("仿宋",12))
        self.label.place(x=5,y=120)
        self.WordPath_entry = tk.Entry(self.frame,width=50)
        self.WordPath_entry.place(x=90,y=120)
        self.OpenWord_button = tk.Button(self.frame, text="打开",width=6,command=self.OpenWordPath,font=("仿宋",12))
        self.OpenWord_button.place(x=460,y=120)
        self.WordTest_button = tk.Button(self.frame, text="测试",width=6,command=self.WordPrintTest,font=("仿宋",12))
        self.WordTest_button.place(x=520,y=120)
        self.WordPath_entry.insert(0,self.WordDefault_path)

        #pdf路径选择及设置按钮
        self.label = tk.Label(self.frame,text="Pdf路径:",font=("仿宋",12))
        self.label.place(x=5,y=160)
        self.PdfPath_entry = tk.Entry(self.frame,width=50)
        self.PdfPath_entry.place(x=90,y=160)
        self.OpenPdf_button = tk.Button(self.frame, text="打开",width=6,command=self.OpenPdfPath,font=("仿宋",12))
        self.OpenPdf_button.place(x=460,y=160)
        self.PdfTest_button = tk.Button(self.frame, text="测试",width=6,command=self.PdfPrintTest,font=("仿宋",12))
        self.PdfTest_button.place(x=520,y=160)
        self.PdfPath_entry.insert(0,self.PdfDefault_path)    

        #excel路径选择及设置按钮
        self.label = tk.Label(self.frame,text="Excel路径:",font=("仿宋",12))
        self.label.place(x=5,y=200)
        self.ExcelPath_entry = tk.Entry(self.frame,width=50)
        self.ExcelPath_entry.place(x=90,y=200)
        self.OpenExcel_button = tk.Button(self.frame, text="打开",width=6,command=self.OpenExcelPath,font=("仿宋",12))
        self.OpenExcel_button.place(x=460,y=200)
        self.ExcelTest_button = tk.Button(self.frame, text="测试",width=6,command=self.ExcelPrintTest,font=("仿宋",12))
        self.ExcelTest_button.place(x=520,y=200)
        self.ExcelPath_entry.insert(0,self.ExcelDefault_path)    

        #ppt路径选择及设置按钮
        self.label = tk.Label(self.frame,text="PPT路径:",font=("仿宋",12))
        self.label.place(x=5,y=240)
        self.label.config(state='disabled') 
        self.PPTPath_entry = tk.Entry(self.frame,width=50)
        self.PPTPath_entry.place(x=90,y=240)
        self.PPTPath_entry.config(state='disabled') 
        self.OpenPPT_button = tk.Button(self.frame, text="打开",width=6,command=self.OpenPPTPath,font=("仿宋",12))
        self.OpenPPT_button.place(x=460,y=240)
        self.OpenPPT_button.config(state='disabled') 
        self.PPTTest_button = tk.Button(self.frame, text="测试",width=6,command=self.PPTPrintTest,font=("仿宋",12))
        self.PPTTest_button.place(x=520,y=240)
        self.PPTTest_button.config(state='disabled') 
        self.PPTPath_entry.insert(0,self.PPTDefault_path) 
        self.PPTPath_entry.config(state='disabled') 

        #Txt路径选择及设置按钮
        self.label = tk.Label(self.frame,text="Txt路径:",font=("仿宋",12))
        self.label.place(x=5,y=280)
        self.TXTPath_entry = tk.Entry(self.frame,width=50)
        self.TXTPath_entry.place(x=90,y=280)
        self.OpenTXT_button = tk.Button(self.frame, text="打开",width=6,command=self.OpenTXTPath,font=("仿宋",12))
        self.OpenTXT_button.place(x=460,y=280)
        self.TXTTest_button = tk.Button(self.frame, text="测试",width=6,command=self.TXTPrintTest,font=("仿宋",12))
        self.TXTTest_button.place(x=520,y=280)
        self.TXTPath_entry.insert(0,self.TXTDefault_path)  

    def get_printers(self):
        # 获取所有打印机的名称
        printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)
        return [printer[2] for printer in printers]  # 打印机名称在元组的第3个元素
    def OneClickTest(Self):
        pass
    def CancelTeam(self):
        pass
    def PauseTask(self):
        pass
    def RecoveryTask(self):
        pass
    #打开图片路径
    def OpenImagePath(self):
        FilePath = filedialog.askopenfilename(title="选择图片文件",filetypes=[("Image Files","*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if FilePath:
            self.ImagePath_enrty.delete(0,tk.END)
            self.ImagePath_enrty.insert(0,FilePath)

    def ImagePrintTest(self):
        file_path = self.ImagePath_enrty.get()
        printer_name = self.Printer_entry.get()
        if not os.path.exists(file_path):
            messagebox.showerror("错误", f"文件 {file_path} 不存在！")
            return
        # 打开图片
        image = Image.open(file_path)
        # 获取指定打印机设备上下文
        hdc = win32ui.CreateDC()
        hdc.CreatePrinterDC(printer_name)  # 使用打印机设备名称

        # 开始打印任务
        hdc.StartDoc("Python Print")
        hdc.StartPage()

        # 绘制位图
        dib = ImageWin.Dib(image)
        dib.draw(hdc.GetHandleOutput(), (0, 0, image.width, image.height))

        # 结束打印任务
        hdc.EndPage()
        hdc.EndDoc()
        hdc.DeleteDC()

    #打开word路径
    def OpenWordPath(self):
        FilePath = filedialog.askopenfilename(title="选择Word文件",filetypes=[("Word Files","*.docx;*.doc")])
        if FilePath:
            self.WordPath_entry.delete(0,tk.END)
            self.WordPath_entry.insert(0,FilePath)
    def WordPrintTest(self):
        file_path = self.WordPath_entry.get()
        printer_name = self.Printer_entry.get()
        if not os.path.exists(file_path):
            messagebox.showerror("错误", f"文件 {file_path} 不存在！")
            return
        try :
            word = win32com.client.Dispatch("Word.Application")
            doc = word.Documents.Open(file_path)
            word.ActivePrinter = printer_name
            doc.PrintOut()
            doc.Close(False)
            # 退出 Word
            if 'word' in locals():
                word.Quit()
        except Exception as e:
            messagebox.showerror("打印失败", f"打印时发生错误: {e}")

    #打开Pdf路径
    def OpenPdfPath(self):
        FilePath = filedialog.askopenfilename(title="选择Pdf文件",filetypes=[("Pdf Files","*.pdf;*.PDF")])
        if FilePath:
            self.PdfPath_entry.delete(0,tk.END)
            self.PdfPath_entry.insert(0,FilePath)
    def PdfPrintTest(self):
        file_path = self.PdfPath_entry.get()
        printer_name = self.Printer_entry.get()
        if not os.path.exists(file_path):
            messagebox.showerror("错误", f"文件 {file_path} 不存在！")
            return
        win32api.ShellExecute(
            0, "print", file_path, f'/d:"{printer_name}"', ".", 0
        )
    
    #打开Excel路径
    def OpenExcelPath(self):
        FilePath = filedialog.askopenfilename(title="选择Excel文件",filetypes=[("Excel Files","*.xls;*.xlsx")])
        if FilePath:
            self.ExcelPath_entry.delete(0,tk.END)
            self.ExcelPath_entry.insert(0,FilePath)
    def ExcelPrintTest(self):
        file_path = self.ExcelPath_entry.get()
        if not os.path.exists(file_path):
            messagebox.showerror("错误", f"文件 {file_path} 不存在！")
            return
        try :
            excel = win32com.client.Dispatch("Excel.Application")
            workbook = excel.Workbooks.Open(file_path)
            sheet = workbook.Sheets(1)  # 选择第一个工作表
            sheet.PrintOut()  # 打印当前工作表
            workbook.Close(False)  # 不保存更改
            excel.Application.Quit()
        except Exception as e:
            messagebox.showerror("打印失败", f"打印时发生错误: {e}")
    #打开PPT路径
    def OpenPPTPath(self):
        FilePath = filedialog.askopenfilename(title="选择PPT文件",filetypes=[("PPT Files","*.ppt;*.pptx")])
        if FilePath:
            self.PPTPath_entry.delete(0,tk.END)
            self.PPTPath_entry.insert(0,FilePath)
    def PPTPrintTest(self):
        file_path = self.PPTPath_entry.get()
        printer_name = self.Printer_entry.get()
        win32print.SetDefaultPrinter(printer_name)

        if not os.path.exists(file_path):
            messagebox.showerror("错误", f"文件 {file_path} 不存在！")
            return
        # 创建 PowerPoint 应用程序对象
        try :
            powerpoint = win32com.client.Dispatch("PowerPoint.Application")
            powerpoint.Visible = 1  # 使 PowerPoint 应用程序可见

            # 打开 PPT 文件
            presentation = powerpoint.Presentations.Open(file_path, WithWindow=False)
            presentation.PrintOut()
            presentation.Close()
            powerpoint.Quit()
        except Exception as e:
            print(f"e={e}")
            messagebox.showerror("打印失败", f"打印时发生错误: {e}")
    #打开TXT路径
    def OpenTXTPath(self):
        FilePath = filedialog.askopenfilename(title="选择Txt文件",filetypes=[("Txt Files","*.txt")])
        if FilePath:
            self.TXTPath_entry.delete(0,tk.END)
            self.TXTPath_entry.insert(0,FilePath)
    def TXTPrintTest(self):
        file_path = self.TXTPath_entry.get()
        printer_name = self.Printer_entry.get()
        if not os.path.exists(file_path):
            messagebox.showerror("错误", f"文件 {file_path} 不存在！")
            return
        win32api.ShellExecute(
            0, "print", file_path, f'/d:"{printer_name}"', ".", 0
        )

if __name__ == "__main__":

    root = tk.Tk()
    app = Driver_Test(root)
    root.mainloop()