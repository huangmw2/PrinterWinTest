import tkinter as tk
from PIL import Image, ImageTk

def on_enter(event):
    button.config(image=img2)

def on_leave(event):
    button.config(image=img1)

root = tk.Tk()

# 加载图片
img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\q\Desktop\自动化测试\测试工具\打印机测试工具开发\自定义工具V2\自定义工具\Hover=false.png"))
img2 = ImageTk.PhotoImage(Image.open(r"C:\Users\q\Desktop\自动化测试\测试工具\打印机测试工具开发\自定义工具V2\自定义工具\Hover=true.png"))

# 创建按钮
button = tk.Button(root, image=img1)
button.pack()

# 绑定事件
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

root.mainloop()
