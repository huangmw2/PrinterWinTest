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


class QueueHandlder:
    def __init__(self):
        self.write_queue = queue.Queue(maxsize=max_size_queue)
        self.read_queue = queue.Queue()
        self.running = True

    def write_to_queue(self, item, item_name = "null"):
        if not self.write_queue.full():
            self.write_queue.put(item)
            log = ">>>>>> 写入队列任务：{} <<<<<<".format(item_name)
            log_message(log,logging.DEBUG)
        else :
            log_message("队列任务以满，请稍后在写入",logging.INFO)

    def read_from_queue(self,comtype):
        max_chunk_size = 32_768
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
    def Print_QRCode(self,QrcodeData,nWidth = 2,nVersion = 0,nErrlevenl = 4):
        ret = Comm_class.Print_QRCode(QrcodeData,nWidth,nVersion,nErrlevenl)
        return ret
    
    def start_read_thread(self,comtype):
        log = "新增一个读队列线程："
        log_message(log,logging.DEBUG)
        read_thread = threading.Thread(target=self.read_from_queue,args=(comtype,))
        read_thread.start()
        return read_thread
    
    def stop_read_thread(self):
        self.running = False
        log = "关闭读队列线程"
        log_message(log,logging.DEBUG)


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
