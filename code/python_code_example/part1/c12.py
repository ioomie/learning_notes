import threading
import time
from threading import current_thread

# 继承threading中的Thread类
class MyThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("start",self.name)

        threadLock.acquire()
        print_time(self.name,self.counter,3)

        threadLock.release()


def print_time(threadName,delay,counter):
        while counter:
            time.sleep(delay)
            print("%s:%s"%(threadName,time.ctime(time.time())))
            counter -= 1

# 线程锁在这里
threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print("Exiting Main Thread")



