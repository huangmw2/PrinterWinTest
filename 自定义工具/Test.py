import socket
import tkinter as tk
from tkinter import messagebox

# 设置服务器的IP地址和端口
server_ip = '192.168.0.204'  # 替换为你的服务器IP
server_port = 9100        # 替换为你的服务器端口

class TCPClientApp:
    def __init__(self, master):
        self.master = master
        self.master.title("TCP Client")
        self.master.geometry("400x300")
        # 创建 TCP 套接字并连接到服务器
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((server_ip, server_port))
            print("连接到服务器成功")
        except Exception as e:
            messagebox.showerror("错误", "连接失败: " + str(e))
            master.destroy()  # 关闭窗口

        # 创建并放置按钮
        self.send_button = tk.Button(master, text="发送数据", command=self.send_data)
        self.send_button.pack(pady=20)

        # 窗口关闭时断开连接
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def send_data(self):
        try:
            message = bytes.fromhex("12 54")
            self.client_socket.sendall(message)
            messagebox.showinfo("信息", "数据发送成功: " + message.hex())
        except Exception as e:
            messagebox.showerror("错误", "发送数据失败: " + str(e))
            print(f"e={e}")

    def on_closing(self):
        # 关闭套接字并退出
        self.client_socket.close()
        print("连接已关闭")
        self.master.destroy()

# 创建主窗口
root = tk.Tk()
app = TCPClientApp(root)

# 运行主循环
root.mainloop()
