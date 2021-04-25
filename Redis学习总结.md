# 什么是Nosql

>泛指非关系型数据库

 NoSQL  = No Only SQL

普通的关系型数据库已经很难用于存储当时时代下所产生的一些数据（动态的，地理位置的等等）

## 特点

1. 方便拓展（数据之间没有关系，很好扩展）解耦

2. 大数据量高性能（Redis 一秒写8万次，写11万次）

3. 数据类型多样型（不需要事先设计数据库）

4. 传统数据库 和 NoSQL

   ```
   传统的数据库
   - 结构化组织
   - SQL
   - 数据和关系都存在单独的表中
   - 严格的一致性
   - 基础的事务
   ```

   ```
   NoSQL
   - 不仅仅是数据
   - 没有固定的查询语言
   - 键值对存储，列存储，文档存储，图形数据库
   - 最终一致性
   - CAP定理 BASE （异地多活）
   - 高性能，高可用，高可拓展
   ```

3V+3高

3V：描述问题

- 海量
- 多样
- 实时

3高：对程序的要求

- 高并发
- 高可拓（随时水平拆分）
- 高性能

两个类型的数据库结合使用

# 架构演进

> 没有什么是加一层是解决不了的

![image-20210425160137040](E:\images\image-20210425160137040.png)

# NoSQL的四大分类

## KV键值对

- Redis

## 文档型数据库

- MongoDB

## 列存储

- HBase

## 图型数据库

- Neo4J

# Redis概述与安装

> 远程字典服务（Remote Dictionary Server）
>
> C编写
>
> 可持久化

## 作用

- 内存存储、持久化（RDB、AOF）
- 效率高，可以用于高速缓存
- 发布订阅系统
- 地图信息分析
- 计时器、计数器

## 特性

- 开源
- 支持多种数据类型
- 数据持久化
- 多语言开发
- 事务控制

## 关于安装

### Windows

Redis的github下获取

### Linux

首先官网下载安装包

```
wget 安装包
```

解压

```
tar -zxvf xxxxx.tar.gz
```

解压后进入到文件内make

```
make
make
make install
```

最终的目录：/usr/loacl/bin

![image-20210425165630637](E:\images\image-20210425165630637.png)

拷贝原配置文件

```
mkdir xxxconfig
cp /xxx/xxx/xxx xxxconfig
```

![image-20210425165950246](E:\images\image-20210425165950246.png)

后台启动

![image-20210425170135163](E:\images\image-20210425170135163.png)

启动Redis（通过指定的配置文件）

```
redis-server xxxx/redis.conf

# 用redis-cli连接
redis-cli -p 6379
```

![image-20210425170523084](E:\images\image-20210425170523084.png)

查看进程

![image-20210425170820723](E:\images\image-20210425170820723.png)

关闭Redis服务 

```
# 在客户端里面使用
shutdown
```

![image-20210425170953965](E:\images\image-20210425170953965.png)



## 简单的使用（Win）

![image-20210425163726585](E:\images\image-20210425163726585.png)

默认端口为：6379

![image-20210425163709478](E:\images\image-20210425163709478.png)

# 性能测试

Redis性能测试工具

```
redis-benchmark -c 100 -n 100000
```

# 基础知识

redis默认有16个数据库，默认使用第0个

可以使用select切换数据库

```bash
[root@VM-0-3-centos bin]# redis-cli 
127.0.0.1:6379> SELECT 0
OK
127.0.0.1:6379> SELECT 1
OK
127.0.0.1:6379[1]> 
```

查看当前数据的的大小

```
127.0.0.1:6379> DBSIZE
(integer) 4
```

查看当前数据库的所有Keys

```
127.0.0.1:6379> KEYS *
1) "myhash"
2) "mylist"
3) "counter:__rand_int__"
4) "key:__rand_int__"
```

清空当前数据库

```
127.0.0.1:6379> FLUSHDB
OK
127.0.0.1:6379> KEYS *
(empty array)
```

清空所有数据库的内容

```
127.0.0.1:6379[1]> FLUSHALL
OK
127.0.0.1:6379[1]> SELECT 0
OK
127.0.0.1:6379> keys *
(empty array)
127.0.0.1:6379> 
```

**Redis是单线程的（版本五之前，六之后就有多线程了）**

Redis基于内存操作，cpu不是瓶颈，而是根据机器的内存和网络带宽

为什么单线程还会这么快

*首先多线程不一定就是比单线程效率高*

核心：redis是将所有数据全部放在内存中，使用单线程效率最高，没有上下文的切换效率最高

# 五大数据类型

## Redis-Key

判断键是否存在

```
127.0.0.1:6379> EXISTS name
(integer) 1
127.0.0.1:6379> EXISTS name1
(integer) 0
127.0.0.1:6379> 
```

将key移动到某个库

```
127.0.0.1:6379> move name 1
(integer) 1
127.0.0.1:6379> 
```

设置值的过期时间

```
# 设置name的过期时间
127.0.0.1:6379> EXPIRE name 10
(integer) 1

# 用ttl能够看到当前的过期时间
127.0.0.1:6379> ttl name
(integer) 7
127.0.0.1:6379> 

```

删除指定key

```
127.0.0.1:6379> set name ioomie
OK
127.0.0.1:6379> keys *
1) "name"
127.0.0.1:6379> del name
(integer) 1
127.0.0.1:6379> 
```

查看key的类型

```
127.0.0.1:6379> set name ioomie
OK
127.0.0.1:6379> type name
string
127.0.0.1:6379> 
```

## String

字符串追加

```
127.0.0.1:6379> APPEND name thirtyseven
(integer) 17
127.0.0.1:6379> get name
"ioomiethirtyseven"
127.0.0.1:6379> 
```

获取字符串长度

```
127.0.0.1:6379> STRLEN name
(integer) 17
127.0.0.1:6379> 
```

自增计数器

```
127.0.0.1:6379> set number 0
OK
127.0.0.1:6379> INCR number
(integer) 1
127.0.0.1:6379> INCR number
(integer) 2
127.0.0.1:6379> INCR number
(integer) 3
127.0.0.1:6379> INCR number
(integer) 4
127.0.0.1:6379> INCR number
(integer) 5
127.0.0.1:6379> INCR number
(integer) 6
127.0.0.1:6379> get number
"6"
127.0.0.1:6379> 
```

自减计数器

```
127.0.0.1:6379> DECR number
(integer) 1
127.0.0.1:6379> DECR number
(integer) 0
127.0.0.1:6379> DECR number
(integer) -1
127.0.0.1:6379> DECR number
(integer) -2
127.0.0.1:6379> DECR number
(integer) -3
127.0.0.1:6379> 
```

设置步长自增自减

```
127.0.0.1:6379> INCRBY number 10
(integer) 7
127.0.0.1:6379> DECRBY number 5
(integer) 2
127.0.0.1:6379> 
```

获取字符串片段 get range

```
127.0.0.1:6379> set number hello,thirtyseven
OK
127.0.0.1:6379> get number
"hello,thirtyseven"
127.0.0.1:6379> GETRANGE number 2 5
"llo,"
127.0.0.1:6379> GETRANGE number 0 -1
"hello,thirtyseven"
```

替换字符串片段 set range

```
127.0.0.1:6379> SETRANGE number 6 ioomie
(integer) 17
127.0.0.1:6379> get number
"hello,ioomieseven"
127.0.0.1:6379>
```

创建一个kv并设置过期时间

```
setex keytex 60 "ioomie"
```

创建一个kv如果存在则无法被修改

*如果key不存在，创建key；如果key存在，创建失败*

```
127.0.0.1:6379> set key4 ioomie
OK
127.0.0.1:6379> SETNX key4 thirtyseven
(integer) 0
127.0.0.1:6379> get key4
"ioomie"
```

设置多个值

```
127.0.0.1:6379> MSET k1 v1 k2 v2 k3 v3
OK
127.0.0.1:6379> keys *
1) "k3"
2) "k2"
3) "k1"
127.0.0.1:6379> 
```

拿取多个值

```
127.0.0.1:6379> mget k1 k2 k3
1) "v1"
2) "v2"
3) "v3"
127.0.0.1:6379> 
```

也有 `msetnx`的用法

这里涉及到原子操作：要么一起成功，要么一起失败，不会出现k1失败 k4成功的现象，只会出现k1的失败导致所有的k都失败

```
127.0.0.1:6379> MSETNX k1 v111 k2 v222 k4 v444
(integer) 0
```

key的巧妙设计

设计一个对象，其值为json字符

key:{id}:{filed}

set user:1:{name:ioomie,age:20}

```
127.0.0.1:6379> mset user:1:name ioomie user:1:age 10
OK
127.0.0.1:6379> mget user:1:name user:1:age
1) "ioomie"
2) "10"
127.0.0.1:6379> 
```

get和set的组合命令

```
127.0.0.1:6379> getset db redis
(nil)
127.0.0.1:6379> get db
"redis"
127.0.0.1:6379> getset db mysql
"redis"
127.0.0.1:6379> get db
"mysql"
127.0.0.1:6379> 
```

### 使用场景

- 字符串
- 计数器
- 数值统计
- 对象缓存

## List

基本数据类型，列表

可用作栈、队列、阻塞队列

列表插值

```
# 头插法
127.0.0.1:6379> LPUSH list one
(integer) 1
127.0.0.1:6379> LPUSH list two
(integer) 2
127.0.0.1:6379> LPUSH list three
(integer) 3
127.0.0.1:6379> LRANGE list 0 -1
1) "three"
2) "two"
3) "one"

# 尾插法
127.0.0.1:6379> RPUSH list one
(integer) 1
127.0.0.1:6379> RPUSH list two
(integer) 2
127.0.0.1:6379> RPUSH list three
(integer) 3
127.0.0.1:6379> LRANGE list 0 -1
1) "one"
2) "two"
3) "three"
127.0.0.1:6379> 
```

移除

```
# 左移除

# 右移除
```



## Set

## Hash

## Zset

# 三种特殊数据类型

## gepspatial

## hyperloglog

## bitmaps