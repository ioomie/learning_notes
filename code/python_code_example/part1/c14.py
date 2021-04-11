import threading
import time

'''
    我想这个例子可能并不太好
'''
list_ = [i for i in range(1000000)]

def open_write(filename):
    it = iter(list_)
    time.sleep(1)
    with open(filename, "a") as f:
        for i in it:
            f.write("%d\n" % (i))
            # print(i)
        f.close()


def open_clear(filename):
    with open(filename, "w") as f:
        f.close()

for i in range(1,11):
    filestr = "test"+str(i)+".txt"
    open_clear(filestr)

start = time.time()
for i in range(1,11):
    filestr = "test"+str(i)+".txt"
    open_write(filestr)
end = time.time()
time1 = end-start
print(time1)

for i in range(1,11):
    filestr = "test"+str(i)+".txt"
    open_clear(filestr)

start = time.time()
t1 = threading.Thread(target=open_write, args=("test1.txt",))
t2 = threading.Thread(target=open_write, args=("test2.txt",))
t3 = threading.Thread(target=open_write, args=("test3.txt",))
t4 = threading.Thread(target=open_write, args=("test4.txt",))
t5 = threading.Thread(target=open_write, args=("test5.txt",))
t6 = threading.Thread(target=open_write, args=("test6.txt",))
t7 = threading.Thread(target=open_write, args=("test7.txt",))
t8 = threading.Thread(target=open_write, args=("test8.txt",))
t9 = threading.Thread(target=open_write, args=("test9.txt",))
t10 = threading.Thread(target=open_write, args=("test10.txt",))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()

end = time.time()
time2 = end-start
print(time2)

