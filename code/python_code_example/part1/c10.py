
import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("耗费时间：",end-start)
    return wrapper

# 语法糖
@timer
def funccccc():
    for i in range(0,100000000):
        pass

funccccc()

# 传参版本
def timer_v2(func):
    def wrapper(*args):
        func(args[0],args[1])
        print("输入的参数个数",len(args))
    return wrapper

def timer_v3(func):
    def warpper(**kwargs):
        for k,v in kwargs.items():
            func(k,v)
        print("输入的键值对个数",len(kwargs))
    return warpper

@timer_v2
def fun_2(x,y):
    print(x*y)

@timer_v3
def fun_3(x,y):
    print("key: %s | value: %s" %(x,y))

fun_2(2,4)
fun_3(num1 = 3,num2 = 5)

# 装饰器可选参数
# 可以利用参数实现更高级的用法
def d1(choose):

    if choose == "add_c":
        def add(func):
            def warpper(*args):
                print("做个加法：", end="")
                func(args[0],args[1])
            return warpper
        return add

    elif choose == "sub_c":
        def sub(func):
            def warpper(*args):
                print("做个减法：",end="")
                func(args[0],args[1])
            return warpper
        return sub

@d1("add_c")
def add(x,y):
    print(x+y)

@d1("sub_c")
def sub(x,y):
    print(x-y)

add(2,4)
sub(4,3)