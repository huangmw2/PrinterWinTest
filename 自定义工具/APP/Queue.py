#读写队列
import threading
import queue
import time 
import logging
try:
    from APP.Usbcom import Comm_class  # 绝对导入
    from APP.Log import log_message
except ImportError:
    from Usbcom import Comm_class  # 相对导入
    from Log import log_message  # 相对导入    

max_size_queue = 100
Queue_Comtype = None

class QueueHandlder:
    def __init__(self):
        self.write_queue = queue.Queue(maxsize=max_size_queue)
        self.read_queue = queue.Queue(maxsize=max_size_queue)
        self.running = True
        self.Rrunning = True

    def write_to_queue(self, item, item_name = "null"):
        if not self.write_queue.full():
            self.write_queue.put(item)
            log = ">>>>>> 写入队列任务：{} <<<<<<".format(item_name)
            log_message(log,logging.DEBUG)
        else :
            log_message("队列任务以满，请稍后在写入",logging.INFO)

    def receive_queue(self,comtype,update_callback=None):
        ret_data = 0XFF
        while self.Rrunning:
            if comtype == "USB":
                ret_data = Comm_class.Read_Usbdata()
            elif comtype == "串口":
                ret_data = 0XFF
            if not self.read_queue.full() and ret_data != 0xFF:
                self.read_queue.put(ret_data)
                update_callback(ret_data)
                log = ">>>>>> 读取到数据：{} <<<<<<".format(ret_data)
                log_message(log,logging.DEBUG)               
                time.sleep(0.01)
        log = "清空接收队列"
        log_message(log,logging.DEBUG)
        self.read_queue.queue.clear()
        self.Rrunning = True

    def read_from_queue(self,comtype):
        max_chunk_size = 32_768
        global Queue_Comtype
        Queue_Comtype = comtype

        while self.running:
            if not self.write_queue.empty():
                item = self.write_queue.get()
                dlength = len(item)
                pack_num = 0
                if dlength > max_chunk_size:
                    for i in range(0, dlength, max_chunk_size):
                        pack_num+=1
                        chunk = item[i:i + max_chunk_size]
                        log = ">>>>>> 任务第{}包  <<<<<<".format(pack_num)
                        log_message(log,logging.DEBUG)
                        self.Send_data(comtype, chunk)
                else :
                    self.Send_data(comtype,item)
                self.write_queue.task_done()
            time.sleep(0.5)
        log = "清空任务队列"
        log_message(log,logging.DEBUG)
        self.write_queue.queue.clear()
        #重新为True，否则下次进来不会发执行读队列
        self.running = True

    def Get_ComType(self):
        return Queue_Comtype
    
    def Send_data(self,Com_type,Data=0):
        if Com_type == "USB":
            result = Comm_class.Write_Usbdata(Data)
            if result > 0:
                log = ">>>>>> 任务发送成功，返回：{}  <<<<<<".format(result)
                log_message(log,logging.INFO)
            else :
                log = ">>>>>> 任务发送失败，返回：{}，请检查端口是否断开 <<<<<<".format(result)
                log_message(log,logging.INFO)

        elif Com_type == "串口":
            Comm_class.Write_serialCom(Data)
        else :
            print("Other Com")
            pass

    def Print_QRCode(self,QrcodeData,nWidth = 2,nVersion = 0,nErrlevenl = 4,Databytes=0):
        global Queue_Comtype
        ret = False
        if Queue_Comtype == "USB":
            ret = Comm_class.Print_QRCode(QrcodeData,nWidth,nVersion,nErrlevenl)
        elif Queue_Comtype == "串口":
            ret = self.Send_data(Queue_Comtype,Databytes)
        else :
            pass
        
        return ret
    
    def Print_Image(self,Imagepath,nWidth = 384,nBinaryAlgorithm=0):
        log = "发送打印图片任务：Path:{}",format(Imagepath)
        log_message(log,logging.DEBUG)
        ret = Comm_class.Print_Image(Imagepath,nWidth,nBinaryAlgorithm)
        if ret:
            log = "任务成功"
        else :
            log = "任务失败"
        log_message(log,logging.DEBUG)
        return ret
            
    def start_read_thread(self,comtype):
        log = "新增一个读队列线程："
        log_message(log,logging.DEBUG)
        read_thread = threading.Thread(target=self.read_from_queue,args=(comtype,))
        read_thread.start()
        return read_thread
    
    def start_receive_thread(self,comtype,update_callback):
        if comtype == "USB":
            log = "新增一个接收数据的线程队列："
            log_message(log,logging.DEBUG)
            read_thread = threading.Thread(target=self.receive_queue,args=(comtype,update_callback))
            read_thread.start()
            return read_thread
           
    def stop_read_thread(self):
        global Queue_Comtype
        self.running = False
        log = "关闭读队列线程"
        log_message(log,logging.DEBUG)
        if Queue_Comtype == "USB":
            self.Rrunning = False
            log = "关闭接收队列线程"
            log_message(log,logging.DEBUG)
            Comm_class.Close_ReadUsbData()

queue_handler = QueueHandlder()

    # 使用示例
if __name__ == "__main__":

    # 启动读取线程
    read_thread = queue_handler.start_read_thread("USB")

    # 让主线程休眠一段时间以观察读取
    try:
        time.sleep(20)  # 运行20秒
    except KeyboardInterrupt:
        print("手动停止")
    # 停止读取线程
    queue_handler.stop_read_thread()
    read_thread.join()
