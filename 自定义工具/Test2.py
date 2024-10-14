import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, root):
        # 主Frame
        self.frame = ttk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # 基础设置
        self.Basic_frame = ttk.LabelFrame(self.frame, text="基础设置", width=680, height=180)
        self.Basic_frame.place(x=0, y=0)

        # Part 1 Frame
        self.Part1_frame = ttk.LabelFrame(self.Basic_frame, text="Part 1", width=250, height=150)
        self.Part1_frame.place(x=0, y=0)
        self.Part1_frame.grid_propagate(False)  # 禁止根据内容自动调整大小

        # 波特率
        self.baud_label = tk.Label(self.Part1_frame, text="波特率:", width=10)
        self.baud_label.grid(row=0, column=0, padx=1, pady=1, sticky="w")  # 仅使用sticky="w"靠左对齐

        self.baud_rate = ttk.Combobox(self.Part1_frame, values=["9600", "19200", "38400", "57600", "115200"], state="readonly", width=10)
        self.baud_rate.grid(row=0, column=1, padx=1, pady=1, sticky="w")
        self.baud_rate.set("9600")  # 默认值

        # 流控
        self.flow_label = tk.Label(self.Part1_frame, text="流控:", width=10)
        self.flow_label.grid(row=1, column=0, padx=1, pady=1, sticky="w")
        self.flow_control = ttk.Combobox(self.Part1_frame, values=["硬件流控", "软件流控"], state="readonly", width=10)
        self.flow_control.grid(row=1, column=1, padx=1, pady=1, sticky="w")
        self.flow_control.set("硬件流控")  # 默认值

        # 设置语言
        self.language_label = tk.Label(self.Part1_frame, text="设置语言:", width=10)
        self.language_label.grid(row=2, column=0, padx=1, pady=1, sticky="w")

        self.encoding = ttk.Combobox(self.Part1_frame, values=["UTF-8", "GBK", "ASCII"], state="readonly", width=10)
        self.encoding.grid(row=2, column=1, padx=1, pady=1, sticky="w")
        self.encoding.set("UTF-8")  # 默认值

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
