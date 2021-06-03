# 版本管理的演变

- 集中式
- 分布式

# Git的特点

- 最优的存储能力
- 强性能
- 开源
- 容易做备份
- 支持离线操作
- 容易定制工作流程

# 安装

[参考官方网址](https://git-scm.com/downloads)

# 简单配置

## 配置user信息

```
git config --global user.name '名字'
git config --global user.email '邮箱'
```

关于参数

![image-20210601162457530](E:\images\image-20210601162457530.png)

- local 对当前的仓库有效
  如果在某个git仓库中有效
- global 对当前用户的所有仓库有效
- system 对系统登录的用户有效

# 建立仓库

两种情景

1. 把已有项目代码纳入git管理

   ```
   cd 某个文件夹
   git init
   ```

2. 新建的项目直接用git管理

   ```
   cd 某个文件夹
   git init 项目名称
   cd 项目名称
   ```

![image-20210601163108330](E:\images\image-20210601163108330.png)

创建后进行配置

![image-20210601163333254](E:\images\image-20210601163333254.png)

**local的优先级高于global**

![image-20210601183701990](E:\images\image-20210601183701990.png)