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

ls -ld 配合使用用于显示当前目录自身的信息

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

## 用户的管理

![image-20210412131009290](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412131009290.png)

新建用户：useradd 用户名称

用户是否存在：id 用户名称

root用户的根目录：/root

普通用户的根目录：/home/用户名/

/etc/passwd /etc/shadow 用户添加后会添加相关信息到这两个文件

只有管理员才能创建用户

设置用户密码：passwd 用户名

删除用户：userdel 用户名

删除用户的时候默认不加-r（userdel -r 用户名）会保留用户的家目录的文件夹

修改用户属性：usermod 选项 用户名
如修改用户的根目录 usermod -d /home/xxx 用户名（相当于给用户的根目录进行了一次搬家）

修改用户属性：chage

![image-20210412131607904](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412131607904.png)

新建用户组 groupadd 用户组

删除用户组 groupdel 用户组

可以将用户的用户组进行修改：
usermod -g 用户组 用户名

也可以在新建用户的同时就加入组：
useradd -g 用户组 用户名

![image-20210412132133716](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412132133716.png)

切换用户 su - 用户名

/etc/passwd

![image-20210412133720456](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412133720456.png)

- 用户名
- 是否需要密码
- 用户id
- 用户所在组id
- 用户的根目录
- 注释字段
- 用户登录成功后进入的解释器

可以利用该文件手动创建一个用户

/etc/shadow

存放用户密码

![image-20210412134352253](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412134352253.png)

/etc/group

![image-20210412134516035](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412134516035.png)

- 组的名称
- 是否需要密码
- 组的id
- 其他组用户的名字（表示这个用户在都属性这两个组）

## 文件权限

![image-20210412134747986](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412134747986.png)

### 文件类型

![image-20210412135046694](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412135046694.png)

![image-20210412135224174](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412135224174.png)

文件权限中一共有9个字符，三个为一组

### 修改文件权限

![image-20210412135426976](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412135426976.png)

![image-20210412141311818](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412141311818.png)

 chown 属主:属组

目录的可执行操作是x，若没有x则无法进入目录

### 特殊权限

![image-20210412143019320](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412143019320.png)

# Vim

## 有四种模式：

- 正常模式
- 插入模式
- 命令模式
- 可视模式

## 关于光标位置：

![image-20210411204621773](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210411204621773.png)

以上图为例，图片中绿色的是光标本身，新的字符会从光标的前面，也就是绿色盖住的d字符前面添加字符，黄色区域的会跟着字符往后走

## 普通模式

### 进入插入模式的命令：

i：进入到当前光标所在位置

shift+i：进入到光标所在行的开头

a：进入到当前光标所在位置的下一个光标位

shift+a：进入到光标所在行的末尾

o：进入到光标所在行的下一行并产生一条空行，将下面原有的行向下推

shift+o：进入到光标所在的上一行并产生一条空行，将下面原有的行像下推

------

v：进入到视图模式

冒号进入到命令模式（shitf+;）

hjkl：在普通模式下对应 **左上下右** 光标的移动

y：复制 yy复制当行 数字+yy复制多行（该行下面的行），y$复制从光标到行尾

d：剪切 dd剪切一整行 数字+dd剪切多行（该行下面的行），d$剪切从光标到行尾

u：撤销上次操作，可多次撤销

ctrl+r：复原上次的撤销

x：删除单个字符

r：替换当个字符

gg：跳转到第一行

shift+g：按行移动光标 数字+shift+g移动到输入的数字行（配合set nu使用）如果不输入数字直接是跳转到最后一行

^：移动到该行的行头

$：移动到该行的末尾

## 命令模式

:w 保存的文件名 保存文件

:q! 不保存退出

:! 可以执行一条linux的命令

/字符 查找字符，按n可以查找匹配到的下一个字符，shift+n查找上一个

:s/旧字符/新字符 替换，这种替换只会针对光标所在的那行进行替换

:%s/旧字符/新字符 全文搜索替换第一个(单次替换)

:%s/旧字符/新字符/g 全局替换

:起始行,结束行s/旧字符/新字符/g 对指定行内的字符进行全局替换

:set nu 显示行号 :set nonu 不显示行号

vim配置文件设置：
/etc/vimrc | /etc/virc

进入到配置文件后可以添加相关的命令进行操作（如添加打开后就显示行号的功能set nu）

## 可视模式

![image-20210412125215377](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412125215377.png)

v 按字符选取

shift+v 按行选取

ctrl+v 可视块

当选中字符后按d可以删除字符

# 管理

## 网络管理

![image-20210412143941408](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412143941408.png)

网络状态查看

- net-tools
- iproute2

root用户：ifconfig 查看网络信息

普通用户：/sbin/ifconfig

修改网卡的名字：

![image-20210412144229435](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412144229435.png)

![image-20210412144854188](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412144854188.png)

查看网卡物理连接情况，主要是网线连接状态

```
mii-tool eth0
```

查看网关

```
route -n
```

修改网络配置

![image-20210412151450105](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412151450105.png)

![image-20210412151503472](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412151503472.png)

![image-20210412151517982](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412151517982.png)

```
修改网络接口参数
ifconfig eth0 10.3.35.147 netmask 255.255.255.0

设定网卡的启动
ifup eth0
ifdown eth0

网关添加和删除
如果默认地址为0.0.0.0为默认网关default
route add default gw xxxxxxxxxx
route del xxxxxxxxxxxxxxxxxxxxx
```

故障排除

![image-20210412152640810](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412152640810.png)

- ping	判断是否畅通
- tarceroute 判断线路间路由的情况
- mtr 网络连通性判断工具
- nslookup 查看域名指向的ip地址
- telnet 判断端口是否能连接
- tcpdump 抓包工具
- netstat -ntpl 用于检测整个Linux系统的网络情况，如服务的启动等
- ss -ntpl 同netstat

服务管理

![image-20210412161441448](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412161441448.png)

![image-20210412161453449](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412161453449.png)

网络接口配置文件目录：

```
/etc/sysconfig/network-scripts/
```

可以进去后进行修改

修改后可利用命令生效：

```
service network restart
```

主机名修改

```
临时修改
hostname ....

非临时
hostnamectl set-hostname xxxxxxxx
修改后需要到 /etc/hosts 中添加对应的主机名

```

## 软件管理

软件安装：

![image-20210412165348984](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412165348984.png)

```
yum redhat 红帽
apt-get ubuntu 乌邦图
```

rpm包安装

![image-20210412174912261](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412174912261.png)

挂载u盘

```
mount
```

当rpm安装软件的时候要打出全名，当用于查询和卸载的时候只需要软件的名称即可

yum安装配置文件：

```
先备份
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup

更换源
/etc/yum.repos.d/CentOS-Base.repo

wget -O /etc/yum.repos.d/CentOS-Linux-BaseOS.repo http://mirrors.aliyun.com/repo/Centos-8.repo

换完后需要更新缓存
yum makecache
```

![image-20210412180414504](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412180414504.png)

源代码编译安装

![image-20210412181142261](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412181142261.png)

1. 下载软件包
2. 解压缩
3. 进入到源代码目录
4. 执行configure文件，configure，将文件放在指定的文件（--prefix=/xxx/xxx/xxx）
5. 编译源文件
6. 执行安装

内核安装

![image-20210412183535098](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412183535098.png)

![image-20210412183547973](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412183547973.png)

![image-20210412183602303](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412183602303.png)

![image-20210412183652917](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412183652917.png)

安装拓展包模块：

```
yum install epel-release -y
```

安装最新的内核：

```
yun install kernel
```

grub引导

![image-20210412184400293](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210412184400293.png)

使用grub修改个人密码

*这里先暂时放下*

## 进程管理

*概念略过*

查看命令

```
ps

pstree

top

进程是个树形的结果
进程和权限有很大关系

ps -e
查看其他进程

ps -ef
显示信息拓展

ps -eLf
线程查看（轻量级进程）

进入top后按数字1可以展示所有的cpu单核情况
修改信息更新时间按s修改
```

Linux的第一个进程：

进程的优先级

![image-20210413113004067](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210413113004067.png)

决定进程优先级

```
nice -n xxx(-20~19) ./xxxxxxxx
PR的值会因为nice的改动而改动
renice -n xxx 进程号(PID)
```

进程的前后台切换

```
将进程于后台运行
./xxxx &

将后台的进程调回前台
fg 进程编号(在切换到后台的时候会有显示)

将前台进程放置后台挂起
ctrl+z

将挂起的程序恢复到后台运行
bg 进程编号

运用jobs可以查看正在运行的进程
```

进程通信：信号

```
kill -l
查看kill命令的信号

杀死进程的信号
kill -9 进程PID

```

守护进程（daemon）

关于nohup

> - 阻止`SIGHUP`信号发到这个进程。
> - 关闭标准输入。该进程不再能够接收任何输入，即使运行在前台。
> - 重定向标准输出和标准错误到文件`nohup.out`。

```
nohup xxxxxxx &

这个作用是可以在命令行关闭之后也能继续执行该进程的命令

这里可以开一个node服务器做试验

server.js代码
var http = require('http');
  
http.createServer(function(req,res){
        res.writeHead(200,{'Content-Type':'text/plain'});
        res.end('成功收到消息啦！');
}).listen(5000);

在后台给个防火墙权限
firewall-cmd --zone=public --add-port=5000/tcp

然后可以用postman或者浏览器访问自己的网址加端口
浏览器可能会乱码
```

screen

多重视窗管理程序

```
screen
创建终端

screen xxx(vi xxxx)
创建终端并执行相关命令

ctrl+a d
退出当前终端

screen -ls
查看所有的终端

screen -r xxxxxxx(终端名字)
重新连接离开的终端

screen -S xxx(一般是前面的几个数字) -X quit
删除终端
```

关于日志所在位置：

```
/var/log
这里面包含了很多的日志记录如系统启动时的内核输出，安全日志等
```

## 服务管理

service

systemctl

首先关于init命令：

- 0 halt 关机
- 1 single user mode 单用户模式
- 2 multiuser 多用户，无网络功能
- 3 full multiuser 多用户 有网络功能
- 4 unused 未定义
- 5 x11 图形桌面坏境
- 6 reboot 重启

我们可以利用init命令进入到不同的运行级别

![image-20210413162956592](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210413162956592.png)

```
system enable|disable xxx 决定服务是否开机启动
```

## 安全管理

*先暂时放下firewall*

SELinux

![image-20210413164232698](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210413164232698.png)

在实际的生产服务器中该功能会比较消耗性能（大量的警报输出）

```
/etc/selinux/config
修改config文件中的SELINUX的选项并重启 可以一直保持修改后的等级
```

## 内存和磁盘管理

### 内存查看

```
free 可以搭配参数 -m -g 以不同的单位进行查看
只查看内存信息

top
```

关于Swap的作用：

> 如果服务器出现了问题并且我们把虚拟内存给禁用了，比如服务器的实际内存爆满，这时候Linux会有一个很恐怖的机制：**随机kill掉几个占用内存最大的进程**

### 磁盘查看

```
fdisk -l
查看硬件盘以及其分区

parted -l
同上，格式不同

df
查看相关分区和目录

du
实际占用空间，有些文件有空洞的占用
```

如何创建一个空的占一定大小的文件：

```
dd
用指定大小的块拷贝一个文件，并在拷贝的同时进行指定的转换

dd if=xxxx(输入的文件) bs=xxM count=xx(复制次数) seek=xx(跳过的区块数) of=xxxx(输出的文件)
```

常见文件系统

![image-20210413192312894](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210413192312894.png)

文件底层结构（ext4）

![image-20210413192455950](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210413192455950.png)

超级块相当于文件系统的地图

i节点记录文件的相关属性如权限等等

> 这里可以解释普通文件和目录文件rwx为什么不同，普通文件中i节点记录的是数据块，而目录文件中的i节点是记录着其他文件的名字，所用读取的方式写入的方式执行的方式都是不同的

链接结构

### 底层相关

首先用touch命令创建一个文件并写入相关的字符（几个就好），然后分别用ls和du查看

```
touch afile
echo 123 > afile
ls -li afile
du -h file
```

这里可以看到在ls中的占用的是特别小的，但是在du中却是一个4K的文件，因为ext4的格式每创建一个数据块都以4K为一个数据块

然后是cp，cp操作会重写创建一个（或好多）数据块，其中的i结点也会不同

随后是mv，mv操作只是改名，其i结点保持不变，他只改了其根目录记录的i结点；如果是移动到其他分分区就会改变其i结点

如果是vim改变了文件内容且没有用硬连接的时候，那文件的i结点会发生改变（echo则不会）

rm，将文件名和i结点断开，其数据块不会被删除

链接两个文件（同一分区）

```
ln file1 file2
```

对两个文件中的其中一个修改都会同时修改

创建软链接（符号链接，非同一分区）

```
ln -s file1 file2
```

文件访问控制列表

```
getfacl xxxx
查看文件的权限

setfacl -m u:(中间可以指定用户，若为空则表示全部):rwx xxx
给文件指定不同用户的不同权限
```

![image-20210413195548796](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210413195548796.png)

### 硬盘的分区挂载

![image-20210413195723262](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210413195723262.png)

格式化和分区操作

```
fdisk /dev/xxx(一般是这样)
```

![image-20210413200531100](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210413200531100.png)

利用+50G的格式将分区设置50G大小

盘符映射

```
mkfs.ext4 (具体按tab查看对应格式) /dev/sda1xxx(这里用fdisk -l查看建立起来分区)
```

硬盘挂载

```
mkdir /mnt/xxxx
创建挂载目录

mount /dev/xxxx(要被挂载的分区) /mun/xxx(刚刚创建的挂载目录)
执行挂载操作
```

![image-20210413201851694](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210413201851694.png)

*注意，这里的挂载是临时的，需要进配置文件添加配置进行固化*

固化操作

进入到/etc/fstab 文件中添加相关参数

![image-20210413202555798](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210413202555798.png)

*为什么要挂载？*

以远程ftp为例，就算我是以root用户登入也无法直接访问硬盘本身：

![image-20210413205659217](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210413205659217.png)

但我可以传输文件到挂载了硬盘的目录：

![image-20210413205852130](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210413205852130.png)

用户磁盘配额

![image-20210413210023978](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210413210023978.png)

### 交换分区

用一个分区创建一个swap

![image-20210413210156093](https://raw.githubusercontent.com/ioomie/learning_notes/master/images-folder/image-20210413210156093.png)