# Linux学习总结

一切皆文件

# 命令大全

## pwd

pwd 显示当前目录

## ls

ls 列出目录内容
ls /root
ls /root /home

### 长格式显示

ls -l

![image-20210406110140408](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210406110140408.png)

从左到右边依次是：

*目录权限，包含文件数，创建用户，用户所属用户组，文件大小，文件创建时间，文件名*

### 显示隐藏文件

ls -a

![image-20210406110742565](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210406110742565.png)

### 逆向显示

默认逆向文件名字

ls -r

以对时间逆向

ls -r -t

### 简化操作

ls -lrt

### 递归显示

ls -R

![image-20210406111045798](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210406111045798.png)

![image-20210406111102006](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210406111102006.png)

## cd

### 绝对路径

cd /xxx/xxx/xxx

### 返回上次目录

cd -

当前目录用 **.** 替代
**.** 和 **/** 可以省略

**..**上级目录

### 返回上级目录

cd ..

![image-20210406113027211](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210406113027211.png)

## 目录操作

### 创建目录

mkdir xxx

mkdir /xxx 在根目录新建

mkdir ./xxx 在当前目录新建 ./ 可以省略

mkdir xxx xxx xxx 创建多目录

无法创建已经存在的目录

mkdir xxx/xxx/xxx 创建多级目录

mkdir -p xxx/xxx/xxx 递归创建 当上级目录不存在的时候也会创建而不是提示找不到该文件

![image-20210406182802549](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210406182802549.png)

*可以利用ls -R xxx 来检查该递归创建的结果*

### 删除目录

rmdir 只能删除空白目录（有其他目录也算有文件）

rm -r 删除目录 非空也能删除

rm -r -f 删除目录且不提示

![image-20210406194834508](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210406194834508.png)

## 复制和移动

cp 单独使用的时候只能复制文件

cp -r 可以复制目录

cp -v 可以查看复制的过程

cp -p 复制过去的时候保存之前的时间不作修改

cp -a 复制所有的信息包括权限

![image-20210406194800460](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210406194800460.png)

## 改名（移动）

用mv操作进行实现

其实在Linux的底层中就是实现了一个移动的操作

mv 旧文件 新文件

![image-20210406194813318](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210406194813318.png)

## 通配符

星号符 有全部的意思

问号 匹配一个字符

![image-20210406194845740](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210406194845740.png)

## 文本查看

cat 文本内容显示到终端

head 查看文件开头

head -5 xxx 5表示显示的行数

tail 查看文件结尾

tail -3 xxx

可以利用参数 -f 同步更新信息

tail -f xxx

wc

![image-20210406194947873](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210406194947873.png)

## 打包压缩

![image-20210406202911068](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210406202911068.png)

### 打包

tar cf /tmp/etc-backup.tar /etc

### 压缩

gzip bzip2

### 打包的同时也压缩了

tar czf /tmp/etc-backup.tar.gz /etc

tar cjf /tmp/etc-backup.tar.bz2 /etc

bzip2的格式的压缩率要高于gzip

### 解包

tar xf xxx -C xxx

tar zxf xxx -C xxx

tar jxf xxx -C xxx

