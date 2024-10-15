import tkinter as tk
from tkinter import ttk

# 创建主窗口
root = tk.Tk()
root.title("K-Printer Setting Tool V2.9")

# 设置窗口大小
root.geometry("500x400")

# 中间的设置黑标模式和取消黑标模式按钮
mode_frame = tk.Frame(root)
mode_frame.pack(pady=10)

set_mode_button = ttk.Button(mode_frame, text="设置黑标模式")
set_mode_button.pack(side=tk.LEFT, padx=20)

cancel_mode_button = ttk.Button(mode_frame, text="取消黑标模式")
cancel_mode_button.pack(side=tk.LEFT, padx=20)

# 创建一个统一的标签输入框和按钮布局
def create_label_entry_button(frame, label_text, entry_value, unit_text, button_text):
    row_frame = tk.Frame(frame)
    row_frame.pack(pady=5, fill="x")
    
    label = tk.Label(row_frame, text=label_text)
    label.pack(side=tk.LEFT, padx=5)
    
    entry = tk.Entry(row_frame, width=10)
    entry.insert(0, entry_value)
    entry.pack(side=tk.LEFT, padx=5)
    
    unit_label = tk.Label(row_frame, text=unit_text)
    unit_label.pack(side=tk.LEFT, padx=5)
    
    button = ttk.Button(row_frame, text=button_text)
    button.pack(side=tk.LEFT, padx=5)

# 创建黑标查找距离、黑标宽度等区域
setting_frame = tk.Frame(root)
setting_frame.pack(pady=10)

create_label_entry_button(setting_frame, "黑标查找距离", "300", "mm", "设置")
create_label_entry_button(setting_frame, "黑标宽度", "40", "mm", "设置")
create_label_entry_button(setting_frame, "找到黑标后进纸", "30", "mm 切纸", "设置")
create_label_entry_button(setting_frame, "找到黑标后进纸", "5", "mm 打印", "设置")

# 底部的三个按钮
bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=20)

buttons_bottom = ["查找黑标", "查找黑标并切纸", "打印测试"]
for text in buttons_bottom:
    button = ttk.Button(bottom_frame, text=text)
    button.pack(side=tk.LEFT, padx=20)

# 运行主循环
root.mainloop()
