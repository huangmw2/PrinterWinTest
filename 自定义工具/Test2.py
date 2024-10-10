import time
import multiprocessing

def write_to_queue(queue):
    for i in range(10, 20):
        queue.put(i)
        print(f"写入：{i}")
        time.sleep(0.5)

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    queue = manager.Queue()  # 使用 Manager 创建共享队列

    write_thread = multiprocessing.Process(target=write_to_queue, args=(queue,))
    write_thread.start()

    write_thread.join()
