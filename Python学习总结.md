# Python3学习总结

## 关于数据类型

在Py中的数据类型有可变和不可变一说，划分如下：

不可变：

- Number 数字 包括int float bool complex（复数）
- String 字符串
- Tuple 元组

可变：

- List 列表
- Dictionary 字典
- Set 集合

*如何理解可变和不可变：*

> 当这些不可变数据类型一旦初始化（赋值）成功后，其对应的在内存地址上的数据本身就不可以有任何变化了
>
> 当对一个不可变数据类型变量进行连续的赋值时，其变量所指向的内存是一直在改变的
>
> 而对于可变类型，在赋值之后是可以改变其内部值数据本身

其中序列包含：

这里序列指成员都是有序排列可以通过下标偏移量访问到它的一个或几个成员

- 字符串
- 列表
- 元组

[这里包含序列操作的例子](https://github.com/ioomie/learning_notes/blob/master/code/python_code_example/part1/c2.py)

### list 列表

定义：一种有序的集合，可以随时添加和删除元素

初始化：

```python
list_test = ["123","456","789"]

# 空列表
list_none = []
```

获取元素：

```python
# 结果为"123"
list_test[0]

# 直接获取最后一个
list_test[-1]
```

添加元素：

```python
# 添加到末尾
list_test.append("abc")

# 指定位置添加
list_test.insert(1,"ABC")
```

删除元素：

```python
# 删除末尾
# 返回删除的值
list_test.pop()

# remove
dict_test.remove("abc")

# 删除指定元素 通过下标指定
list_test.pop(1)
```

修改元素：

```python
list_test[1] = "newstr"
```

### tuple 元组

定义：有序列表，一旦初始化就不能再修改

初始化：

```python
tuple_test = ("123","567")

# 空元组
tuple_none = ()

# 只定义一个元素
tuple_one = (3,)

# 错误定义
# tuple_error = (3)
```

#### "可变"Tuple

```python
tuple_list = ("a","b",["abc","bcd"])

tuple_list[2][0] = "xxx"

# 这里看似修改了元组，实际上是修改了列表
```

#### 关于元组的大小比较

假设现在有元组：

```
tuple1 = (1,20)
tuple2 = (2,18)
```

在比大小中，元组的大小是将两个数字以拼接的方式进行比较：

```
tuple > tuple # False
tuple < tuple # True
```

实际就是 120 跟 218 进行比较 大小就是

### dict 字典

map，采用键值对存储

可以理解为哈希值和对象

初始化：

```python
dict_test = {
	0:"zero",
	1:"one",
	2:"two",
	3:"three"
}
```

查找方法：

```python
# 第一种 通过key查找 但这样会存在key不存在字典而报错的现象
dict_test[0]
dict_test[4]

# 其实可以用 0 in dict_test 的语句判断该key是否在字典中存在

# 第二种 get()方法 当字典中没有该key时可以返回自定义的value
dict_test.get(0,"none")
dict_test.get(4,"none")
```

添加元素：

```python
# 第一种 当字典中不存在该key:value的时候会添加该key
# 如果是存在则相当于修改该key的value
dict_test[4] = "four"
dict_test[0] = "zerooooooooo"

# 第二种 update()
dict_test.update({4:"foerrrrrr"})
# 如果采用这种形式其参数必须是字符串对象
dict_test.update(strkey = "strvalue",strkey_second = "strvalue_second")
```

删除元素：

```
# del
del [dict_test[0]]

# pop
dict_test.pop(0)


# clear 删除所有
dict_test.clear()
```

### set 集合

初始化：

```python
set_test = {1,2,3,4,5}
set_null = set()
# 生成空集合不能使用 set_null = {} 的方式，这个方式生成的是空字典非集合
```

集合中的值是不重复的，如果在初始化的时候有重复值，但在打印的时候只会输出其中的一个

添加元素

```python
# add()
set_test.add(6)

# update()
set_test.update(["one","two"])
set_test.update("abc")
```

删除元素：

```python
set_test.remove(0)
```

### 类型间的转换

## 一些常用函数

### range()

返回一个可迭代对象，非列表类型

需要和 **list**() 函数将迭代对象转换为列表

### filter()

第一个参数为判断函数，可传入自定义函数，也可用lambda表达式

第二个参数为可迭代对象，如列表等

返回一个迭代器对象，可以用list()函数进行转换

例子：

```python
a = [1,2,3,4,5,6,7,8]
list_ = list(filter(lambda x:x%2 == 0,a))
print(list_)
```

### map()

第一个参数为判断函数

第二个对象为一个或多个序列

例子：

```python
a = [1,2,3,4,5,6,7,8]
map_ = list(map(lambda x:x%2 == 0,a))
print(map_)
```

*关于map和filter的区别：*

> map返回的是由True和False组成的迭代器
>
> filter返回的是过滤后的元素而不是True或False本身

### reduce()

用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果

在python3中需要引入functools模块调用

```python
from functools import reduce

sum = reduce(lambda x, y: x+y, [1,2,3,4,5])
print(sum)
```

### zip()

将对象中对应的元素打包成一个个元组，并返回一个对象

例子：

```python
a = [1,2,3]
b = [4,5,6]
dict_ = {1:"one",2:"two"}

# 返回一个可迭代对象
zipbacg = zip(a,b)
for x in zipbacg:
    print(x)
# 解压
print(*zipbacg)

zipdict = zip(dict_.values(),dict_.keys())
# 类似于矩阵转置
print(dict(zipdict))
```

### isupper()

如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False

### split()

通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串

例子：

```python
str = "123|345|789"

# 以"|"的形式进行分割字符，返回列表的格式
print(str.split("|"))
# 将字符串分割成两个字符，遇到的第一个|就分割
print(str.split("|",1))
```

### strip()

用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列

*只能删除开头或是结尾的字符，不能删除中间部分的字符*

例子：

```python
str  = "\n   hahaha   \n"
str_str = "000xixixi000"

# 默认什么都不填为删除空格和换行
print(str.strip())
print(str_str.strip("0"))
```

### replace()

三个参数

1. 将被替换的子字符串
2. 新字符串，用于替换old子字符串
3. 指替换次数，不超过几次，可以不填默认为替换全部

## 推导式

[推导式例子](https://github.com/ioomie/learning_notes/blob/master/code/python_code_example/part1/c3.py)

### 列表推导式

```python
alist = [i*i for i in  range(1,11) if i%2 == 0]
```

### 字典推导式

```python
# 字典推导式
# 这在爬虫的时候会经常用到 如解析cookies
adict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three"
}
bdict = {key:value for key,value in adict.items()}
print(bdict)
```

## IO操作

[文件操作例子](https://github.com/ioomie/learning_notes/blob/master/code/python_code_example/part1/c4.py)

## 进程和线程

多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了

## 关于切片操作

[切片操作例子](https://github.com/ioomie/learning_notes/blob/master/code/python_code_example/part1/c1.py)

## 关于异常

**错误不等于异常**

异常处理流程：

1. 检测到错误，引发异常
2. 对异常进行捕获

异常捕获格式（以打开文件为例子）

```python
try:
    file = open("namb.txt")
except Exception as e:
    print("输出异常")
    print(e)
finally:
    print("不管如何都要将文件进行关闭")
    file.close()
```

### 上下文管理器

with语句，当出现异常的时候会自动执行关闭文件对象的语句

[异常的处理的例子](https://github.com/ioomie/learning_notes/blob/master/code/python_code_example/part1/c5.py)

## 自定义函数

### 关键字参数

```
# 如print中的end为关键字参数
print("xxx",end="我是个结尾")
```

### 可变长参数

#### *args

这是一个可变参数列表

返回一个元组

```
# 可变参数
def arglist(*args):
    for str in args:
        print(str)


arglist("123", "456", "789")
```

#### **kwargs

这是一个可变的关键字参数（字典）

返回一个字典

```
# 可变的关键字参数(字典)
def kvdict(**kwargs):
    for k, v in kwargs.items():
        print("%s -> %s" % (k, v))


kvdict(k1=123, k2=456, k3=789)

```

[可变长参数例子](https://github.com/ioomie/learning_notes/blob/master/code/python_code_example/part1/c6.py)

## 迭代器&生成器

为什么使用迭代器？

> 1. 不依赖索引取值
> 2. 节省内存

示例：

```python
# 迭代器生成
list_ = [1,2,3]
it = iter(list_)
print(next(it))
print(next(it))
print(next(it))
# 最后一个会报错
print(next(it))
```

一些普通的简单的迭代器不适用于我们一些平常的列子比如使用range函数的时候步长必须是整数不能是小数，这个时候就需要用生成器构建自己的迭代器：

```python
# 返回一个迭代器
def frange(start,end,step):
    x = start
    while x<end:
        yield x
        x += step
```

[迭代器和生成器实例](https://github.com/ioomie/learning_notes/blob/master/code/python_code_example/part1/c7.py)

## lambda表达式

一般配合一些函数使用

```
lambda x:xxx
# 输入的参数:返回结果中运行的语句
```

[lambda实例](https://github.com/ioomie/learning_notes/blob/master/code/python_code_example/part1/c8.py)

## 闭包

在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用，这样就构成了一个闭包。

[闭包实例](https://github.com/ioomie/learning_notes/blob/master/code/python_code_example/part1/c9.py)

## 装饰器

允许向一个现有的对象添加新的功能，同时又不改变其结构。

```python
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end-start)
    return wrapper

# 语法糖
@timer
def funccccc():
    for i in range(0,100000000):
        pass
```

一些细分的用法在实例中展示

[装饰器实例](https://github.com/ioomie/learning_notes/blob/master/code/python_code_example/part1/c10.py)

*闭包和装饰器*

> 因为闭包最大的特点就是封装上下文，能够维持一个结构去不断复用而不用改变去改变内部的结构
>
> 如果将现有的函数和闭包混合，比如计时器的案例，这可以在我们添加新的函数时候对于一些功能直接进行复用而不是重写
>
> 如果有许多新的函数需要被编写而其中有些函数的功能是一样的有些是不一样的，这时候装饰器的作用就开始展现出来了
>
> 通过装饰器语法糖的时候可以非常非常轻松去完成一个功能的调用，如函数的计时器，如果我想给这个函数加个计时器则直接运用语法糖的形式便可

## 类和类的继承