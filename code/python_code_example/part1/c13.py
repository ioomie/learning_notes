import threading
import time

listA = []
listB = []
listC = []
listD = []
list_ = []

def add(list_,x,y):
    # time.sleep(2)
    for i in range(x,y):
        # print(i)
        list_.append(i)

start = time.time()
t1 = threading.Thread(target=add,args=(listA,0,25000000))
t2 = threading.Thread(target=add,args=(listB,25000000,50000000))
t3 = threading.Thread(target=add,args=(listC,50000000,75000000))
t4 = threading.Thread(target=add,args=(listD,75000000,100000000))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

list_all = listA+listB+listC+listD
end = time.time()
print(end - start)
print(len(list_all))

start = time.time()
add(list_,0,100000000)
end = time.time()
print(end - start)
print(len(list_))
