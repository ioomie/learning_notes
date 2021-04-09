
# 迭代器生成
list_ = [1,2,3]
it = iter(list_)
# print(next(it))
# print(next(it))
# print(next(it))
# 最后一个会报错
# print(next(it))

for x in it:
    print(x)

# 生成器
# 带yield的迭代器
def frange(start,end,step):
    x = start
    while x<end:
        yield x
        x += step
'''
    在函数中运用了yield后 函数会返回一个迭代器
    yield很像一个输出print
    如果是从表面理解就一个是输出到控制台，一个则是输出到迭代对象里
    如果不用输出的方式而是转存列表的方式
    当数据量非常庞大的时候数组就会占用更多的内存空间
    而迭代器占用的内存会很少
'''
for x in frange(10,20,0.5):
    print(x)