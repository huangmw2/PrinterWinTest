import json
import os
import threading
from tkinter import messagebox
if __name__ == "__main__":
    from logger import log_message  
else :
    try:
        from APP.logger import log_message 
    except ImportError:
        from logger import log_message 
import logging

class ConfigParas:
    _instance = None
    _lock = threading.Lock()  # 用于线程安全

    def __new__(cls):
        ''' 
            单例模式：所有模块共享一个实例
        '''
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(ConfigParas, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.config_data = None
        self.ConfigPath = None
        Current_DIR = os.getcwd()
        self.ConfigPath = os.path.join(Current_DIR, r"Data\Config\Config.json")

        if os.path.exists(self.ConfigPath):
            with open(self.ConfigPath, 'r', encoding='utf-8') as file:
                try:
                    self.config_data = json.load(file)
                except Exception as e:
                    log = "配置文件数据错乱，错误信息：{}".format(e)
                    log_message(log,logging.ERROR)
                    self.config_data = None
        else :
            log = "文件:{}不存在。".format(self.ConfigPath)
            log_message(log,logging.ERROR)
    
    def get_config_data(self):
        return self.config_data

    def get_config_item(self,key):
        value = None
        value = self.config_data[key]
        return value
    
    def modify_all_data(self,data):
        self.config_data = data

    def Modify_Data(self,*args, value=None):
        if not self.config_data:
            return False
        if not args:
            log = "未传入字段名，无法修改。"
            log_message(log,logging.ERROR)
            return False
        data = self.config_data
        # 如果只传入一个字段，则直接修改该字段的值
        if len(args) == 1:
            key = args[0]
            if key in data:
                data[key] = value
                log = "更新{} 字段的值为{}".format(key,value)
                log_message(log,logging.DEBUG)
                return True
            else:
                log = "字段 {} 不存在".format(key)
                log_message(log,logging.ERROR)
                return False
        else :
            # 使用 *args 导航 JSON 的多层级结构
            for key in args[:-1]:  # 遍历到倒数第二个层级
                if key in data:
                    data = data[key]
                else:
                    log = "字段 {} 不存在(2)".format(key)
                    log_message(log,logging.ERROR)
                    return False
            if args[-1] in data:
                data[args[-1]] = value
                log = "更新{} 字段的值为{}".format(args[-1],value)
                log_message(log,logging.DEBUG)
                return True
            else:
                log = "字段 {} 不存在(2)".format(args[-1])
                log_message(log,logging.ERROR)
                return False
        
    def Add_Data(self,*args, value=None):
        if not self.config_data:
            return False
        if not args:
            log = "未传入字段名，无法修改。"
            log_message(log,logging.ERROR)
            return False
        # 如果是单层级情况，直接添加到顶层
        if len(args) == 1:
            key = args[0]
            if key in self.config_data:
                log = "字段 {} 存在,无法添加".format(key)
                log_message(log,logging.ERROR)
                return False
            else:
                self.config_data[key] = value
                log = "添加{} 字段的值为{}".format(key,value)
                log_message(log,logging.DEBUG)
                return True
        else :
            data = self.config_data
            try:
                for key in args[:-1]:  # 遍历到倒数第二个层级
                    if key not in data or not isinstance(data[key], dict):
                        # 如果路径中的层级不存在，自动创建
                        data[key] = {}
                    data = data[key]  # 进入下一级

                # 在目标位置添加新字段
                if args[-1] in data:
                    log = "字段已存在{}，无法添加".format(args[-1])
                    log_message(log,logging.ERROR)
                    return False
                else:
                    data[args[-1]] = value
                    log = "添加{} 字段的值为{}".format(args[-1],value)
                    log_message(log,logging.DEBUG)
                    return True
            except Exception as e:
                log = "添加字段过程中出现异常:{}".format(e)
                log_message(log,logging.ERROR)
                return False

    def Save_Data(self):
        if not self.config_data:
            return False
        try:
            with open(self.ConfigPath, 'w', encoding='utf-8') as f:
                json.dump(self.config_data, f, ensure_ascii=False, indent=4)
                return True
        except Exception as e:
            messagebox.showerror("错误", "保存json参数数据失败")
            return False
        
#Config_Data = ConfigParas()

if __name__ == "__main__":
    app = ConfigParas()
    app.Modify_Data("Serial_number",value="COM5")
    app.Add_Data("TSPL_delay22",value="COM5")