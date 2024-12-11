#Netword Test
import tkinter as tk
from tkinter import ttk

class Netword_Test:
    def __init__(self,parent):
        self.frame =tk.Frame(parent,bd=2,relief=tk.GROOVE)
        self.frame.pack(fill=tk.BOTH,expand=True)
        #网络
        NetWorkSet_frame = ttk.LabelFrame(self.frame, text="网络设置")
        NetWorkSet_frame.place(x=0,y=0,width=350,height=220)
        #ip设置
        self.IP_label = tk.Label(NetWorkSet_frame,text="IP 地址：")
        self.IP_label.place(x=0,y=5)
        self.IP_entry = tk.Entry(NetWorkSet_frame, width=14)
        self.IP_entry.place(x=60,y=5)
        self.IP_entry.insert(0,"192.168.0.87")
        #子网掩码设置
        self.Netmask_label = tk.Label(NetWorkSet_frame,text="子网掩码：")
        self.Netmask_label.place(x=180,y=5)
        self.Netmask_entry = tk.Entry(NetWorkSet_frame, width=14)
        self.Netmask_entry.place(x=240,y=5)
        self.Netmask_entry.insert(0,"255.255.255.0")
        #网关设置
        self.Gatway_label = tk.Label(NetWorkSet_frame,text="网关：")
        self.Gatway_label.place(x=0,y=30)
        self.Gatway_entry = tk.Entry(NetWorkSet_frame, width=14)
        self.Gatway_entry.place(x=60,y=30)
        self.Gatway_entry.insert(0,"192.168.0.1")
        #端口
        self.Port_label = tk.Label(NetWorkSet_frame,text="端口：")
        self.Port_label.place(x=180,y=30)
        self.Port_entry = tk.Entry(NetWorkSet_frame, width=14)
        self.Port_entry.place(x=240,y=30)
        self.Port_entry.insert(0,"9100")
        #SSID
        self.BroadcastName_label = tk.Label(NetWorkSet_frame,text="SSID:")
        self.BroadcastName_label.place(x=0,y=60)
        self.BroadcastName_entry = ttk.Combobox(NetWorkSet_frame, width=25)
        self.BroadcastName_entry.place(x=60,y=60)
        #密码
        self.Passwd_label = tk.Label(NetWorkSet_frame,text="密码:")
        self.Passwd_label.place(x=0,y=90)
        self.Passwd_entry = tk.Entry(NetWorkSet_frame, width=25)
        self.Passwd_entry.place(x=60,y=90)

        self.WIFI_Scan_button = tk.Button(NetWorkSet_frame, text="扫描",width=8,command=self.WIFIScan)
        self.WIFI_Scan_button.place(x=260,y=60)
        self.ipmode_option = tk.StringVar()
        self.ipmode_option.set("dhcp")
        self.DHCPIp_WIFI = tk.Radiobutton(NetWorkSet_frame, text="动态IP", variable=self.ipmode_option, value="dhcp")
        self.DHCPIp_WIFI.place(x=220,y=90)
        self.Static_Ip_WIFI = tk.Radiobutton(NetWorkSet_frame, text="静态IP", variable=self.ipmode_option, value="static")
        self.Static_Ip_WIFI.place(x=280,y=90)
        
        #打开网口
        self.OpenNetwork_button = tk.Button(self.frame, text="打开网口",width=8,command=self.Up_Eth)
        self.OpenNetwork_button.place(x=0,y=140)
        #关闭网关
        self.CloseNetwork_button = tk.Button(self.frame, text="关闭网口",width=8,command=self.Down_Eth)
        self.CloseNetwork_button.place(x=70,y=140)
        #设置网口参数
        self.EthSet_button = tk.Button(self.frame, text="网口设置",width=8,command=self.Set_Eth)
        self.EthSet_button.place(x=140,y=140)       

        #设置WIFI
        self.WIFISet_button = tk.Button(self.frame, text="WIFI设置",width=8,command=self.Set_WIFI)
        self.WIFISet_button.place(x=140,y=170)
        #关闭网关
        self.CloseWIFI_button = tk.Button(self.frame, text="关闭WIFI",width=8,command=self.Down_WIFI)
        self.CloseWIFI_button.place(x=70,y=170)

        #self.BroadcastName_entry.insert(0,"")
        #以太网
        NetWorkTest_frame = ttk.LabelFrame(self.frame, text="网络测试")
        NetWorkTest_frame.place(x=350,y=0,width=350,height=220)

        self.PingIp_label = tk.Label(NetWorkTest_frame,text="Ip:")
        self.PingIp_label.place(x=0,y=5)    
        self.PingIp_entry = tk.Entry(NetWorkTest_frame, width=14)
        self.PingIp_entry.place(x=30,y=5)  

        self.Number_label = tk.Label(NetWorkTest_frame,text="次数:")
        self.Number_label.place(x=140,y=5)    
        self.Number_entry = tk.Entry(NetWorkTest_frame, width=6)
        self.Number_entry.place(x=180,y=5)  
        #Ping测试
        self.PingTest_button = tk.Button(NetWorkTest_frame, text="Ping 测试",width=8,command=self.PING_Test)
        self.PingTest_button.place(x=0,y=30)
        #TCP测试
        self.TCPTest_button = tk.Button(NetWorkTest_frame, text="TCP 测试",width=8,command=self.TCP_Test)
        self.TCPTest_button.place(x=70,y=30)         
        #停止
        self.Stop_button = tk.Button(NetWorkTest_frame, text="停止",width=8,command=self.StopButton)
        self.Stop_button.place(x=140,y=30) 
        #蓝牙
        BluetoothSet_frame = ttk.LabelFrame(self.frame, text="蓝牙设置")
        BluetoothSet_frame.place(x=0,y=225,width=350,height=240)
        #蓝牙名称
        self.BTName_label = tk.Label(BluetoothSet_frame,text="蓝牙名称：")
        self.BTName_label.place(x=0,y=5)
        self.BTName_entry = ttk.Combobox(BluetoothSet_frame, width=14)
        self.BTName_entry.place(x=60,y=5)

        self.SCan_button = tk.Button(BluetoothSet_frame, text="扫描",width=8,command=self.BTScan)
        self.SCan_button.place(x=200,y=5)

        #双模蓝牙名称
        self.BT2Name_label = tk.Label(BluetoothSet_frame,text="双模名称：")
        self.BT2Name_label.place(x=0,y=30)
        self.BT2Name_entry = tk.Entry(BluetoothSet_frame, width=14)
        self.BT2Name_entry.place(x=60,y=30)

        #蓝牙密码
        self.BTPasswd_label = tk.Label(BluetoothSet_frame,text="蓝牙密码")
        self.BTPasswd_label.place(x=0,y=55)
        self.BTPasswd_entry = tk.Entry(BluetoothSet_frame, width=14)
        self.BTPasswd_entry.place(x=60,y=55)

        #蓝牙型号
        self.BTModel_label = tk.Label(BluetoothSet_frame,text="蓝牙型号：")
        self.BTModel_label.place(x=180,y=55)
        self.BTModel_entry = tk.Entry(BluetoothSet_frame, width=14)
        self.BTModel_entry.place(x=240,y=55)  
        #蓝牙模式
        self.BTType_option = tk.StringVar()
        self.BTType_option.set("type2")
        self.BTType1 = tk.Radiobutton(BluetoothSet_frame, text="未安装蓝牙", variable=self.BTType_option, value="type1")
        self.BTType1.place(x=10,y=80)
        self.BTType2 = tk.Radiobutton(BluetoothSet_frame, text="单模蓝牙", variable=self.BTType_option, value="type2")
        self.BTType2.place(x=120,y=80)
        self.BTType3 = tk.Radiobutton(BluetoothSet_frame, text="双模蓝牙", variable=self.BTType_option, value="type3")
        self.BTType3.place(x=220,y=80)
        #密码授权
        self.BTPasswd_option = tk.StringVar()
        self.BTPasswd_option.set("passwd1")
        self.BTPasswd1 = tk.Radiobutton(BluetoothSet_frame, text="需要密码鉴权", variable=self.BTPasswd_option, value="passwd1")
        self.BTPasswd1.place(x=10,y=110)
        self.BTPasswd2 = tk.Radiobutton(BluetoothSet_frame, text="不需要密码鉴权", variable=self.BTPasswd_option, value="passwd2")
        self.BTPasswd2.place(x=180,y=110)
        #设置按钮
        self.BTSet_button = tk.Button(BluetoothSet_frame, text="设置",width=50,command=self.BTParas_set)
        self.BTSet_button.place(x=0,y=150)       

        BluetoothTest_frame = ttk.LabelFrame(self.frame, text="蓝牙测试")
        BluetoothTest_frame.place(x=350,y=225,width=350,height=240)
        #蓝牙名称
        self.BTName2_label = tk.Label(BluetoothTest_frame,text="蓝牙名称：")
        self.BTName2_label.place(x=0,y=5)
        self.BTName2_entry = tk.Entry(BluetoothTest_frame, width=14)
        self.BTName2_entry.place(x=60,y=5)
        #连接
        self.BTConnect_button = tk.Button(BluetoothTest_frame, text="连接",width=8,command=self.BTConnect)
        self.BTConnect_button.place(x=180,y=0)
        #蓝牙信号
        self.BTsignal_label = tk.Label(BluetoothTest_frame,text="蓝牙信号：")
        self.BTsignal_label.place(x=0,y=35)    

        self.BTsignal_entry = tk.Entry(BluetoothTest_frame, width=14)
        self.BTsignal_entry.place(x=60,y=35)

        self.BTSignal_button = tk.Button(BluetoothTest_frame, text="信号测试",width=8,command=self.BTSignalTest)
        self.BTSignal_button.place(x=180,y=35)
        #蓝牙丢包率测试

        #发送蓝牙控制指令
        self.BTSend_frame = ttk.LabelFrame(BluetoothTest_frame,text="蓝牙指令发送")
        self.BTSend_frame.place(x=0,y=70,width=350,height=200)
        self.BTSend_text = tk.Text(self.BTSend_frame, height=6, width=40)
        self.BTSend_text.place(x=0,y=5)  

        self.BTSend_button = tk.Button(BluetoothTest_frame, text="AT指令发送",width=10,command=self.BTSendAT)
        self.BTSend_button.place(x=5,y=180)

    def Up_Eth(self):
        pass
    def Down_Eth(self):
        pass
    def Set_Eth(self):
        pass
    def Set_WIFI(self):
        pass    
    def Down_WIFI(self):
        pass
    def PING_Test(self):
        pass    
    def TCP_Test(self):
        pass
    def StopButton(self):
        pass
    def BTScan(self):
        pass
    def WIFIScan(self):
        pass
    def BTParas_set(self):
        pass
    def BTConnect(self):
        pass
    def BTSignalTest(self):
        pass
    def BTSendAT(self):
        pass