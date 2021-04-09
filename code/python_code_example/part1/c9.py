
def fun_nomal(x,y):
    return x*y

def fun_out(a,b):
    def fun_in(x,y):
        return a*x+b*y
    return fun_in

print(fun_nomal(1,2))

getfun = fun_out(5,10)
print(getfun(1,2))
print(getfun(3,4))
print(getfun(5,6))

# 简单的计数器
'''
    计数器可以复用而不是通过定义全局变量实现
    该闭包传入的时候直接调用一个int类型的变量
    这是一个不可变的类型
    此时如果要在内部函数不通过声明而直接调用
    会因为变量作用域的问题造成报错
    因为在内部没有定义过这个变量，这会造成编译器找不到你这个变量
    所以要使用闭包内的变量需要用nonlocal声明在外层函数定义好的变量
'''
def count(x):
    def count_add():
        nonlocal x
        x += 1
        return x
    return count_add

'''
    这里关于函数
    func() 表示函数的调用，会执行函数里的语句
    func 没有括号叫函数的引用，不会执行函数里的内容
'''
getfun1 = count(5)
getfun2 = count(10)
print(getfun1())
print(getfun1())
print(getfun1())
print(getfun2())
print(getfun2())
print(getfun2())