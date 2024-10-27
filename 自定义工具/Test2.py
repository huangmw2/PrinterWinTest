import tkinter as tk
import queue
import threading
import time

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("接收区示例")
        self.geometry("400x200")

        # 创建接收区和滚动条
        recv_frame = tk.Frame(self)
        recv_frame.pack(pady=10)

        recv_scrollbar = tk.Scrollbar(recv_frame)
        recv_scrollbar.grid(row=0, column=1, sticky="ns")

        self.recv_text = tk.Text(recv_frame, height=6, width=50, yscrollcommand=recv_scrollbar.set)
        self.recv_text.grid(row=0, column=0, padx=1, pady=1)
        recv_scrollbar.config(command=self.recv_text.yview)

        # 十六进制接收选项
        self.Hex_reve_flag = tk.BooleanVar(value=True)
        hex_recv_check = tk.Checkbutton(recv_frame, text="十六进制接收",
                                        variable=self.Hex_reve_flag,
                                        onvalue=True, offvalue=False,
                                        command=self.Hex_model, font=("仿宋", 10))
        hex_recv_check.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        # 数据队列
        self.read_queue = queue.Queue()

        # 开启线程模拟数据接收
        self.Rrunning = True
        threading.Thread(target=self.simulate_data_receiving, daemon=True).start()

        # 定期更新接收区内容
        self.update_recv_text()

    def simulate_data_receiving(self):
        # 模拟接收数据并加入队列
        while self.Rrunning:
            time.sleep(1)  # 模拟数据接收的间隔
            sample_data = "Hello" if not self.Hex_reve_flag.get() else "48 65 6C 6C 6F"
            self.read_queue.put(sample_data)

    def Hex_model(self):
        # 处理十六进制接收模式切换
        print("十六进制模式:", self.Hex_reve_flag.get())

    def update_recv_text(self):
        # 从队列读取数据并显示在接收区
        while not self.read_queue.empty():
            data = self.read_queue.get()
            self.recv_text.insert(tk.END, f"{data}\n")
            self.recv_text.see(tk.END)  # 滚动到底部

        # 继续调用自己，检查新数据
        self.after(100, self.update_recv_text)

    def on_closing(self):
        self.Rrunning = False
        self.destroy()

# 创建应用程序并运行
if __name__ == "__main__":
    app = Application()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
