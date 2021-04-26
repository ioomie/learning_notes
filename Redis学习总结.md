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
127.0.0.1:6379> LPOP list
"one"
127.0.0.1:6379> LRANGE list 0 -1
1) "two"
2) "three"
127.0.0.1:6379> 

# 右移除
127.0.0.1:6379> RPOP list
"three"
127.0.0.1:6379> LRANGE list 0 -1
1) "two"
127.0.0.1:6379> 
```

通过下标获取值

```
127.0.0.1:6379> LINDEX list 1
"two"
127.0.0.1:6379> 
```

返回列表长度

```
127.0.0.1:6379> LLEN list
(integer) 3
127.0.0.1:6379> 
```

移除指定的值

移除为指定的list内设置要移除的个数以及要被移除的值（精确匹配）

```
127.0.0.1:6379> LRANGE list 0 -1
1) "one"
2) "two"
3) "three"
4) "three"
127.0.0.1:6379> LREM list 2 three
(integer) 2
127.0.0.1:6379> LRANGE list 0 -1
1) "one"
2) "two"
127.0.0.1:6379> 
```

截取列表，原list被改变

```
127.0.0.1:6379> LTRIM list 1 2
OK
127.0.0.1:6379> LRANGE list 0 -1
1) "two"
2) "three"
127.0.0.1:6379> 
```

组合操作

移除列表的最右边元素并放到另一个列表的最左边，当然也可以自己给自己操作

*不止是从右边出发，左右都可以*

```
127.0.0.1:6379> LRANGE list 0 -1
1) "two"
2) "three"
127.0.0.1:6379> RPOPLPUSH list list
"three"
127.0.0.1:6379> RPOPLPUSH list list
"two"
127.0.0.1:6379> RPOPLPUSH list list
"three"
127.0.0.1:6379> RPOPLPUSH list list
"two"
127.0.0.1:6379> RPOPLPUSH list list
"three"
127.0.0.1:6379> RPOPLPUSH list list
"two"
127.0.0.1:6379> RPOPLPUSH list list
"three"
127.0.0.1:6379> RPOPLPUSH list listnew
"two"
127.0.0.1:6379> LRANGE list 0 -1
1) "three"
127.0.0.1:6379> LRANGE listnew 0 -1
1) "two"
127.0.0.1:6379> 
```

修改某个下标的值

只有当该列表存在并且该下标的值也存在的时候才能成功修改，否则会发生抱错

```
127.0.0.1:6379> lset list 0 oneeeeeeee
OK
127.0.0.1:6379> LRANGE list 0 -1
1) "oneeeeeeee"
127.0.0.1:6379> lset list 1 oneeeeeeee
(error) ERR index out of range
127.0.0.1:6379> 
```

往某个值的前后进行插值，可以在这个值的前面插入或后面插入

```
127.0.0.1:6379> LINSERT list before two inworld1
(integer) 5
127.0.0.1:6379> LRANGE list 0 -1
1) "four"
2) "three"
3) "inworld1"
4) "two"
5) "one"
127.0.0.1:6379> LINSERT list after two inworld1
(integer) 6
127.0.0.1:6379> LRANGE list 0 -1
1) "four"
2) "three"
3) "inworld1"
4) "two"
5) "inworld1"
6) "one"
127.0.0.1:6379> 
```

> **实际上是一个双向链表，可以前插后插**
>
> **如果key不存在，创建新链表**
>
> **如果key存在，更新链表**
>
> **如果移除所有的值，代表空链表表示不存在**
>
> **两边插入效率最高，中间插入效率不太高**
>
> **可以用来做消息队列，从左边拿进去，从右边拿出来**

## Set

set中的值无法重读，无序不重复集合

创建以sadd的形式创建集合并添加值，利用SMEMBERS查看集合的值，利用SISMEMBER判断该值是否在集合中

```
127.0.0.1:6379> sadd myset hello
(integer) 1
127.0.0.1:6379> sadd myset hello1
(integer) 1
127.0.0.1:6379> sadd myset hello2
(integer) 1
127.0.0.1:6379> SMEMBERS myset
1) "hello"
2) "hello1"
3) "hello2"
127.0.0.1:6379> SISMEMBER myset hello
(integer) 1

# 如果集合中有该值了则会添加失败
127.0.0.1:6379> sadd myset hello
(integer) 0
127.0.0.1:6379> sadd myset hello
(integer) 0

```

获取集合中的元素个数

```
127.0.0.1:6379> scard myset
(integer) 3
```

移除集合中的元素

```
127.0.0.1:6379> SREM myset hello
(integer) 1
127.0.0.1:6379> SMEMBERS myset
1) "hello1"
2) "hello2"
```

随机获取set中的值，可以一次获取多个

```
127.0.0.1:6379> SMEMBERS myset
1) "hello"
2) "hello1"
3) "hello3"
4) "hello2"
5) "hello4"
127.0.0.1:6379> SRANDMEMBER myset
"hello3"
127.0.0.1:6379> SRANDMEMBER myset
"hello4"
127.0.0.1:6379> SRANDMEMBER myset
"hello1"
127.0.0.1:6379> SRANDMEMBER myset 2
1) "hello"
2) "hello3"
127.0.0.1:6379> SRANDMEMBER myset 2
1) "hello3"
2) "hello2"
127.0.0.1:6379> SRANDMEMBER myset 2
1) "hello1"
2) "hello3"
```

随机删除一个集合中的元素

```
127.0.0.1:6379> SMEMBERS myset
1) "hello"
2) "hello1"
3) "hello4"
4) "hello2"
5) "hello3"
127.0.0.1:6379> spop myset
"hello4"
127.0.0.1:6379> SMEMBERS myset
1) "hello"
2) "hello1"
3) "hello2"
4) "hello3"
```

将元素转移到另一个集合

```
127.0.0.1:6379> sadd newset xixixi
(integer) 1
127.0.0.1:6379> SMOVE myset newset hello
(integer) 1
127.0.0.1:6379> SMEMBERS newset
1) "hello"
2) "xixixi"
```

求两个集合的差集

```
127.0.0.1:6379> SDIFF myset newset
1) "hello1"
2) "hello3"
```

求两个集合的交集

```
127.0.0.1:6379> SINTER myset newset
1) "hello"
2) "hello2"
```

求两个集合的并集

```
127.0.0.1:6379> SUNION myset newset
1) "hello3"
2) "hello2"
3) "hello"
4) "hello1"
5) "xixixi"
```

*当然可以参与运算的肯定不只限于两个集合，可以是多个集合*

**将所有关注的人放在一个set集合中，粉丝也是，共同关注的人可以做一个交集**

## Hash

一个map集合

相当于 key-map集合（map中也有键值对）

利用hset创建一个hash，利用hget和hmget以及hgetall获取对应的数据

*hmset被弃用，用hset进行操作*

```
127.0.0.1:6379> hset myhash name ioomie
(integer) 1
127.0.0.1:6379> hget myhash name
"ioomie"
127.0.0.1:6379> HGETALL myhash

# 以一个键一个值的格式展示
1) "name"
2) "thirty"
3) "age"
4) "21"
5) "class"
6) "123123"
7) "gd"
8) "2018"
```

删除指定字段

删除后key-value都会被删除

```
127.0.0.1:6379> HDEL myhash gd
(integer) 1
```

获取hash的长度

```
127.0.0.1:6379> HLEN myhash
(integer) 3
# 表示有三个键值对
```

判断字段是否存在

```
127.0.0.1:6379> HEXISTS myhash name
(integer) 1
```

只获得所有的字段或只获得所有的值

```
127.0.0.1:6379> HKEYS myhash
1) "name"
2) "age"
3) "class"
127.0.0.1:6379> HVALS myhash
1) "thirty"
2) "21"
3) "123123"
127.0.0.1:6379> 
```

自增减、判断是否存在，参考String

**存取一个user的数据，或者购物车**

## Zset（有序集合）

再set的基础上增加了一个排序值

创建zset

```
127.0.0.1:6379> zadd myset 1 one
(integer) 1
127.0.0.1:6379> zadd myset 2 two
(integer) 1
127.0.0.1:6379> zadd myset 3 three
(integer) 1
127.0.0.1:6379> ZRANGE myset 0 -1
1) "one"
2) "two"
3) "three"
```

排序

```
# 默认输出全部的时候会按照从小到大排序
127.0.0.1:6379> ZRANGE myset 0 -1
1) "xixixi"
2) "hahaha"
3) "gegege"

# 降序
127.0.0.1:6379> ZREVRANGE myset 0 -1
1) "gegege"
2) "hahaha"
3) "xixixi"

```

查询分数的区间

```
# 从最小到最大
127.0.0.1:6379> ZRANGEBYSCORE myset -inf +inf
1) "xixixi"
2) "hahaha"
3) "gegege"

# 从0到500
127.0.0.1:6379> ZRANGEBYSCORE myset 0 500
1) "xixixi"
2) "hahaha"

# 可以返回其值
127.0.0.1:6379> ZRANGEBYSCORE myset -inf +inf withscores
1) "xixixi"
2) "100"
3) "hahaha"
4) "500"
5) "gegege"
6) "1000"
```

移除元素

```
127.0.0.1:6379> ZRANGE myset 0 -1
1) "xixixi"
2) "hahaha"
3) "gegege"
127.0.0.1:6379> ZREM myset xixixi
(integer) 1
127.0.0.1:6379> ZRANGE myset 0 -1
1) "hahaha"
2) "gegege"
```

获取有序集合内元素的个数

```
127.0.0.1:6379> ZCARD myset
(integer) 2

```

获取区间内元素的个数

```
127.0.0.1:6379> ZRANGEBYSCORE myset -inf +inf  withscores
1) "xixixi"
2) "100"
3) "hehehe"
4) "300"
5) "hahaha"
6) "500"
7) "gegege"
8) "1000"
127.0.0.1:6379> ZCOUNT myset 200 1000
(integer) 3
```

**带权重的需要排序的场景**

# 三种特殊数据类型

## gepspatial 地理位置

朋友的定位，附近的人

添加地理位置

[GEOADD官方文档](https://redis.io/commands/geoadd)

> 地球两极无法添加（南极北极）
>
> 一般会下载城市数据，通过脚本一次性导入
>
> （经度，纬度，名称）
>
> Valid longitudes are from -180 to 180 degrees.
>
> Valid latitudes are from -85.05112878 to 85.05112878 degrees.

```
127.0.0.1:6379> GEOADD china:city 113.2 23.1 loacl
(integer) 1
127.0.0.1:6379> GEOADD china:city 116.40 39.90 beijing 121.47 31.23 shanghai 106.50 29.53 chongqin
(integer) 3

```

获取城市地标

获取到的一定是个坐标值

```
127.0.0.1:6379> GEOPOS china:city loacl
1) 1) "113.20000022649765015"
   2) "23.10000005307264104"
```

返回两个给定位置的距离

```
127.0.0.1:6379> GEODIST china:city loacl beijing
"1892710.7224"
127.0.0.1:6379> GEODIST china:city loacl beijing km
"1892.7107"
127.0.0.1:6379> 
```

以给定的经纬度为中心，找出某一半径内的元素

```
127.0.0.1:6379> GEORADIUS china:city 110 30 1000 km
1) "chongqin"
2) "loacl"

# 展示经纬度
127.0.0.1:6379> GEORADIUS china:city 110 30 1000 km withcoord
1) 1) "chongqin"
   2) 1) "106.49999767541885376"
      2) "29.52999957900659211"
2) 1) "loacl"
   2) 1) "113.20000022649765015"
      2) "23.10000005307264104"
      
# 展示直线距离
127.0.0.1:6379> GEORADIUS china:city 110 30 1000 km withdist
1) 1) "chongqin"
   2) "341.9374"
2) 1) "loacl"
   2) "830.7525"
   
# 
127.0.0.1:6379> GEORADIUS china:city 110 30 1000 km withhash
1) 1) "chongqin"
   2) (integer) 4026042091628984
2) 1) "loacl"
   2) (integer) 4046510601247634
   
# 以某个城市为原点
127.0.0.1:6379> GEORADIUSBYMEMBER china:city loacl 1000 km
1) "loacl"
2) "chongqin"

```

返回一个hash字符串

```
127.0.0.1:6379> GEOHASH china:city loacl beijing
1) "ws07rvjxr00"
2) "wx4fbxxfke0"
```

删除

*GEO的底层实现为Zset，可以用Zset进行操作*

```
127.0.0.1:6379> ZRANGE china:city 0 -1
1) "chongqin"
2) "loacl"
3) "shanghai"
4) "beijing"
127.0.0.1:6379> ZREM china:city loacl
(integer) 1
```

## hyperloglog

基数（不重复的元素），可以接受误差

用于做基础统计方法

一个人访问一个网站多次，但是还是算作一个人

> 占用内存固定，2^64不同的元素，只需要12kb

利用PFADD创建一个key，用PFMERGE合并两个key，用PFCOUNT对key进行计数

```
127.0.0.1:6379> PFADD mykey a b c d e
(integer) 1
127.0.0.1:6379> PFADD mykey2 c d e f g
(integer) 1
127.0.0.1:6379> PFMERGE mykey3 mykey2 mykey
OK
127.0.0.1:6379> PFCOUNT mykey3
(integer) 7
```

## bitmaps

位存储

统计用户信息、登录、打卡...

两个状态的都可以使用bitmaps

```
127.0.0.1:6379> setbit sign 1 0
(integer) 0
127.0.0.1:6379> setbit sign 2 0
(integer) 0
127.0.0.1:6379> setbit sign 3 1
(integer) 0
127.0.0.1:6379> setbit sign 4 1
(integer) 0
127.0.0.1:6379> setbit sign 5 1
(integer) 0
127.0.0.1:6379> GETBIT sign 1
(integer) 0
127.0.0.1:6379> GETBIT sign 4
(integer) 1

# 有3给1 返回3
127.0.0.1:6379> BITCOUNT sign
(integer) 3
```

# 事务

关系型数据库：ACID（原子性，一致性，隔离性，持久性）

具备原子性：要么同时成功，要么同时失败

**Redis单条命令是保证原子性的，但是，Redis的事务是不能保证原子性的**

事务的本质：一组命令的集合

一个事务中的命令都会被序列化，所有事务的执行过程中都会按照顺序执行

一次性、顺序性、排他性

**Redis没有隔离级别的概念**

在事务中，所有命令并没有被直接执行，只有发起执行命令的时候才会执行

事务执行过程：

- 开启事务（MULTI）
- 命令入队（一堆命令）
- 执行事务（EXEC）

## 正常执行事务

```
127.0.0.1:6379> MULTI
OK
127.0.0.1:6379(TX)> set k1 v1
QUEUED
127.0.0.1:6379(TX)> set k2 v2
QUEUED
127.0.0.1:6379(TX)> get k1
QUEUED
127.0.0.1:6379(TX)> set k3 v3
QUEUED
127.0.0.1:6379(TX)> EXEC
1) OK
2) OK
3) "v1"
4) OK
```

## 放弃事务

事务队列中的所有命令都不会被执行

```
127.0.0.1:6379> MULTI
OK
127.0.0.1:6379(TX)> set k1 v1
QUEUED
127.0.0.1:6379(TX)> DISCARD
OK
```

## 关于错误

### 编译型异常

代码本身，或者命令本身有问题

导致事务中所有的命令都不会被执行

```
127.0.0.1:6379> MULTI
OK
127.0.0.1:6379(TX)> get
(error) ERR wrong number of arguments for 'get' command
127.0.0.1:6379(TX)> set kkkkk vvvvv
QUEUED
127.0.0.1:6379(TX)> EXEC
(error) EXECABORT Transaction discarded because of previous errors.
127.0.0.1:6379> get kkkkk
(nil)
```



### 运行时异常

比如 1/0 的案例

事务中代码没错但不符合逻辑或者语法，其他命令可以正常执行，错误的命令会抛出异常

```
127.0.0.1:6379> MULTI
OK
127.0.0.1:6379(TX)> set k1 string
QUEUED
127.0.0.1:6379(TX)> INCR k1
QUEUED
127.0.0.1:6379(TX)> EXEC
1) OK
2) (error) ERR value is not an integer or out of range
```

**这里可以体现出Redis的事务是不具备原子性的**

# Redis实现乐观锁

## 监控

当多线程执行的时候需要加锁

### 悲观锁

很悲观，什么时候都会出问题，无论做什么都会加锁

### 乐观锁

很乐观，认为什么时候都不会出问题，所以不上锁，更新数据的时候去判断，在此期间是否有人修改过这个数据

获取version

更新的时候比较version

### 监视器

WATCH key

事务执行成功后事务就会取消

正常成功执行

```
127.0.0.1:6379> set money 100
OK
127.0.0.1:6379> set out 0
OK
127.0.0.1:6379> WATCH money
OK
127.0.0.1:6379> MULTI
OK
127.0.0.1:6379(TX)> DECRby money 20
QUEUED
127.0.0.1:6379(TX)> INCRBY out 20
QUEUED
127.0.0.1:6379(TX)> EXEC
1) (integer) 80
2) (integer) 20
```

模拟多线程修改