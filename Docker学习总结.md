# 概念

关于Docker

**简单的虚拟机**

# Docker思想

- 集装箱：把程序运行环境和部署细节进行整体封装，封装后密封，不容易丢失或损坏
- 标准化
  - 运输方式：超级中转站，例如把台式机上的应用部署到笔记本上，PC上运行docker命令，应用被送到了超级中转站，然后在笔记本上运行docker命令，就可以实现应用的整体迁移
  - 存储方式：程序员不需要关心应用存储在什么地方，docker会自动进行标准化处理，程序员只需要运行docker命令调用即可
  - API接口：能够实现执行同样的Docker命令，就可以控制不用的Web应用服务器，例如Tomcat和Nginx等
- 隔离：使用虚拟机，有独立的内存、CPU、硬盘，使得使用者完全感觉不到主机的存在。Docker只需要1秒，就可以创建轻量级的虚拟机，底层技术可以理解为进程资源的隔离

# Docker能干什么

- 运行环境统一：将各个运行环境，例如：Tomcat，JDK，操作系统等分别装入集装箱运送到码头，再由别的机器下载即可
- 公用服务器时互不影响：开发共用服务器时，Docker为每个人分配了固定的CPU，内存，磁盘，不会因为某个人的程序问题影响到别人导致全部资源被用光
- 快速扩展，弹性伸缩：双十一等场合下，需要扩展服务器，采用Docker的标准化API，可以用几个命令来实现快速部署，启动

# Docker相关操作

## 镜像的拉取

```
docker pull 要拉取的镜像名字:镜像的版本
docker pull thirtyseven/universal_centos:latest
```

## 镜像的本地操作

查看

```
docker images
```

删除

```
docker rmi 镜像名字
```

## 容器的生成

```
docker run -d -p xxxx:xx --name xxx 镜像的名字 
下面是创建linux容器的例子
--privileged 用于让容器内的root用户用真的root权限
docker run -itd --privileged -p 4545:22 --name centos_docker centso /usr/sbin/init
```

## 容器操作

查看

```
docker ps

查看所用容器 包括未运行的
docker ps -a
```

启动暂停的容器

```
docker start 容器id，用空号分隔可以启动多个
```

删除

```
docker rm 容器id
```

在运行的容器中执行命令（进入容器）

```
docker exec -it 容器名字（id）
下面是执行linux容器的命令窗口的命令，这样可以进入到该linux容器中执行命令行
docker exec -it centos_docker /bin/bash
```

## 生成本地镜像

commit方式

```
docker commit -a "提交人" -m "提交说明" 容器id 生成的镜像名:版本（标签也叫）
```

Dcokerfile（未使用，待学习）

## push镜像至Docker Hub

登录账号

```
dokcer login
然后输入账号密码
```

push镜像

```
push前要tag修改镜像名 这一步会生成一个新的镜像（内容和之前呢个一样，名字不同而已）
docker tag 镜像名字:镜像版本 用户名/镜像名（这里是自定义的）:镜像版本

然后推送
docker push 用户名/镜像名:镜像版本
其实是
docker push 刚刚改完tag的新镜像全名包括版本
```

