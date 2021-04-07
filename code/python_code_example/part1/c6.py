# 可变参数
def arglist(*args):
    print(type(args))
    for str in args:
        print(str)


arglist("123", "456", "789")


# 可变的关键字参数(字典)
def kvdict(**kwargs):
    print(type(kwargs))
    for k, v in kwargs.items():
        print("%s -> %s" % (k, v))


kvdict(k1=123, k2=456, k3=789)
