CONFIG = {
    #启动窗口的各个参数
    "setup_windows" : {
        "win_title": "测试工具",
        "win_geometry" : "700x500+600+300",
        "comm_option_name" : "选择端口参数",       
        "comm_option_position" : (0,5,260,700),  
        "serial_radiobutton_name" : "串口",
        "serial_radiobutton_position" : (10,10),
        "serial_port_combobox_position" : (80,10),
        "baud_rate_name": "波特率",
        "baud_rate_position" : (200,10),
        "baud_rate_default_value" : "115200",
        "baud_rate_value" : ['2400', '4800', '9600', '19200', '38400', '57600','115200', '230400'],
        "baud_rate_entry_positiopn" : (250,10),
        "serial_parity_name" : "校验方式",
        "serial_parity_name_positiopn" : (360,10),
        "serial_parity_values" : ['NONE', 'ODD', 'EVEN'],
        "serial_parity_entry_positiopn": (400,10),
        "serial_parity_default_values":  "NONE",
        "usb_radiobutton_name" : "USB",
        "usb_radiobutton_position" : (10,40),
        "usb_device_combobox_position": (80,40),
        "eth_radiobutton_name" : "网口",
        "eth_radiobutton_position" : (10,70),
        "eth_ip_entry_position" : (80,70),
        "eth_port_name" : "端口号",
        "eth_port_name_position" : (250,70),
        "eth_port_entry_position" : (310,70),
        "lpt_radiobutton_name" : "网口",
        "lpt_radiobutton_position" : (10,100),
        "lpt_entry_position" : (80,100),
    }
    ,
    "error_display" : {
        "error_name" : "错误",
        "serial_error_code" : {
            "no_device_detected" : "打开端口失败：未检测到串口设备",
            "failed_to_open_port" : "打开串口端口失败"
        },
        "usb_error" : {
             "no_device_detected" : "打开端口失败：未检测到USB设备",
             "failed_to_open_port" : "打开USB端口失败"
        },

        "network_error" : {
            "connection_failed" : "网络连接失败",
        }
    },

    "error_log_message" : {
        "serial_error_code" : {
            "no_device_detected" : "打开端口失败：未检测到串口设备",
            "failed_to_open_port" : "打开串口端口失败"
        },
        "usb_error" : {
            "no_device_detected" : "打开端口失败：未检测到USB设备",
            "failed_to_open_port" : "打开USB端口失败",
        }
    },

    "debug_log_message": {
        "code_1":"打开串口成功(code1)",
        "code_2":"打开USB成功(code2)",
        "code_3":"网络连接成功(code3)",
    }
}