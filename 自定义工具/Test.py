import tkinter as tk
from tkinter import ttk

def create_ui():
    root = tk.Tk()
    root.title("K-Printer Setting Tool V2.9 - 基础设置")

    # 设置窗口大小
    root.geometry("500x400")

    # 基本参数部分
    tk.Label(root, text="波特率:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    baud_rate = ttk.Combobox(root, values=["9600", "19200", "38400", "57600", "115200"], state="readonly")
    baud_rate.grid(row=0, column=1, padx=10, pady=5)
    baud_rate.set("9600")  # 默认值

    tk.Label(root, text="流控:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    flow_control = ttk.Combobox(root, values=["硬件流控", "软件流控"], state="readonly")
    flow_control.grid(row=1, column=1, padx=10, pady=5)
    flow_control.set("硬件流控")  # 默认值

    tk.Label(root, text="设置语言:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    encoding = ttk.Combobox(root, values=["UTF-8", "GBK", "ASCII"], state="readonly")
    encoding.grid(row=2, column=1, padx=10, pady=5)
    encoding.set("UTF-8")  # 默认值

    set_button = tk.Button(root, text="设置", width=10, command=lambda: print("基本参数设置已保存"))
    set_button.grid(row=2, column=2, padx=10, pady=5)

    # 字体设置部分
    tk.Label(root, text="字体设置:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    font_size = ttk.Combobox(root, values=["12x24", "8x16", "16x32"], state="readonly")
    font_size.grid(row=3, column=1, padx=10, pady=5)
    font_size.set("12x24")  # 默认值

    tk.Label(root, text="打印浓度:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    print_density = ttk.Combobox(root, values=["淡淡", "微淡", "正常", "加深"], state="readonly")
    print_density.grid(row=4, column=1, padx=10, pady=5)
    print_density.set("微淡")  # 默认值

    tk.Label(root, text="进纸:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
    paper_feed = ttk.Combobox(root, values=["0x0A", "0x0B", "0x0C"], state="readonly")
    paper_feed.grid(row=5, column=1, padx=10, pady=5)
    paper_feed.set("0x0A")  # 默认值

    set_font_button = tk.Button(root, text="设置", width=10, command=lambda: print("字体设置已保存"))
    set_font_button.grid(row=5, column=2, padx=10, pady=5)

    # 切刀类型和蜂鸣器
    tk.Label(root, text="切刀类型:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
    cutter_type = ttk.Combobox(root, values=["不切", "切纸"], state="readonly")
    cutter_type.grid(row=6, column=1, padx=10, pady=5)
    cutter_type.set("不切")  # 默认值

    buzzer_var = tk.IntVar()
    tk.Checkbutton(root, text="蜂鸣器", variable=buzzer_var).grid(row=6, column=2, padx=10, pady=5)

    knife_var = tk.IntVar()
    tk.Checkbutton(root, text="切刀", variable=knife_var).grid(row=6, column=3, padx=10, pady=5)

    auto_print_last_var = tk.IntVar()
    tk.Checkbutton(root, text="自动打印最后一单", variable=auto_print_last_var).grid(row=7, column=1, padx=10, pady=5)

    set_cutter_button = tk.Button(root, text="设置", width=10, command=lambda: print("切刀类型和蜂鸣器设置已保存"))
    set_cutter_button.grid(row=7, column=2, padx=10, pady=5)

    # 休眠时间和关机时间
    tk.Label(root, text="休眠时间:").grid(row=8, column=0, padx=10, pady=5, sticky="w")
    sleep_time = ttk.Combobox(root, values=["300", "600", "900", "1200"], state="readonly")
    sleep_time.grid(row=8, column=1, padx=10, pady=5)
    sleep_time.set("600")  # 默认值

    tk.Label(root, text="关机时间:").grid(row=9, column=0, padx=10, pady=5, sticky="w")
    shutdown_time = ttk.Combobox(root, values=["3600", "7200", "10800", "14400"], state="readonly")
    shutdown_time.grid(row=9, column=1, padx=10, pady=5)
    shutdown_time.set("7200")  # 默认值

    set_time_button = tk.Button(root, text="设置", width=10, command=lambda: print("休眠时间和关机时间已保存"))
    set_time_button.grid(row=9, column=2, padx=10, pady=5)

    # 恢复默认设置
    reset_button = tk.Button(root, text="恢复默认设置", width=20, command=lambda: print("恢复默认设置"))
    reset_button.grid(row=10, column=1, padx=10, pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_ui()
