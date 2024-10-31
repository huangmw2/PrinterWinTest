# RAM Test
import tkinter as tk
from tkinter import ttk

class RAM_Test:
    def __init__(self,parent):
        self.frame = tk.Frame(parent,bd=2,relief=tk.GROOVE)
        self.frame.pack(fill=tk.BOTH,expand=True)
        if __name__ == "__main__":
            self.root = parent
            self.root.title("RAM测试/设置")
            self.root.geometry("700x500+600+300") 

if __name__ == "__main__":
    root = tk.Tk()
    app = RAM_Test(root)
    root.mainloop()