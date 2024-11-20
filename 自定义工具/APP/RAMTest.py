# RAM Test
import tkinter as tk
from tkinter import ttk

if __name__ == "__main__":
    from  Config import Config_Data
else :
    from APP.Config import Config_Data

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
        self.Fun_frame.place(x=0,y=0,width=380,height=500)
        
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
        self.scrollbar.place(x=350,y=0,height=500)

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
            self.creat_entry_entry_button(self.scrollable_frame,i,key,value,lambda:self.Send_button(i))
            # 输出结果
            print("第一个节点的名称:", self.Entry_1[i].get())
            print("第一个节点的值:", value)
            

    def creat_entry_entry_button(self,frame,_row,text1,cmd,button_fun): 
        entry_1 = tk.Entry(frame, width=13)
        entry_1.grid(row=_row, column=0, padx=5, pady=2,sticky="w")
        entry_1.insert(0,text1)
        self.Entry_1.append(entry_1)

        entry_2 = tk.Entry(frame, width=13)
        entry_2.grid(row=_row, column=1, padx=5, pady=2,sticky="w")
        entry_2.insert(0,cmd)     
        self.Entry_2.append(entry_2)

        button_fun = tk.Button(frame, text="发送",command=button_fun,width=8)
        button_fun.grid(row=_row, column=2, padx=5, pady=1)          

        #return entry_1,entry_2
    
    def Send_button(self,Value):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = RAM_Test(root)
    root.mainloop()