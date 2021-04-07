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

[这里包含序列操作的例子]()

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

## 一些常用函数

### range()

返回一个可迭代对象，非列表类型

需要和 **list**() 函数将迭代对象转换为列表

### filter()

## 推导式

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

[文件操作例子]()

## 进程和线程

多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了

## 关于切片操作

[切片操作例子](https://github.com/ioomie/learning_notes/blob/master/code/python_code_example/part1/c1.py)

## 关于异常

**错误不等于异常**

异常处理流程：

1. 检测到错误，引发异常
2. 对异常进行捕获

