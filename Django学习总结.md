# 简单介绍

一个纯Python编写的web框架

# 安装

一般情况

```
pip install Django
```

非一般情况，这里用Anaconda

```
conda install Django
```

当然有装必有卸

```
conda uninstall Django
```

或者指定版本安装

```
conda install Django==3.2.2
```

[最新的LTS版本可以在这里看](https://www.djangoproject.com/download/)

![image-20210511172353887](E:\images\image-20210511172353887.png)

安装好后版本验证

```
python -m diango --version
```

# 创建项目

简单版（新手版本）

先cd到一个想要存放代码的地方

然后：

```
django-admin startproject xxxxx
```

这样就可以得到一个项目了：

![image-20210510211843882](E:\images\image-20210510211843882.png)

这是一个项目的总体，也就是一个容器，里面会包含很多不同的应用

运行该项目的命令（还是在有manage.py的目录下）后面的` 0:8000`默认如果不写就会在本地回环地址上，并在8000端口上运行该服务器

```
python manage.py runserver 0:8000
```

*这里有个小插曲*

> 在启动服务器之前需要给他一个运行的hosts
>
> ![image-20210511171937431](E:\images\image-20210511171937431.png)
>
> 在上面添加要通过浏览器进行访问的ip地址或域名

然后访问

![image-20210511172113307](E:\images\image-20210511172113307.png)

弹出这个页面表示一个建议的Django项目被创建成功了

随后添加项目内的应用

```
python manage.py startapp xxxxx
```

然后创建一个应用

![image-20210511172540480](E:\images\image-20210511172540480.png)

然后改代码

step1：编写一个视图

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

step2：添加一个urls.py的文件

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

step3：在根URLconf文件中创建我们新建立的模块

```python
from django.contrib import admin
# 加上include模块
from django.urls import include, path

urlpatterns = [
    # 加上刚刚添加的模块
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

然后再访问，这里注意一下url：
![image-20210511172908841](E:\images\image-20210511172908841.png)

这里就表示创建应用成功

# 连接数据库

[关于数据库方面的使用](https://docs.djangoproject.com/zh-hans/3.2/topics/db/)

在默认情况下，Django使用sqlite作为默认数据库，这里我们改用mysql

首先要安装python驱动mysql的库

```
conda install pymysql
```

然后在seting.py中添加数据库的默认设置

![image-20210512135600805](E:\images\image-20210512135600805.png)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 数据库名字
        'NAME': 'imsys',
        # 登录用户
        'USER':'root',
        # 登录密码
        'PASSWORD':'xxx',
        # 登录地址
        'HOST':'127.0.0.1',
        # 登录端口
        'PORT':'3306',
    }
}
```

然后修改时区

> 在上述如果不修改时区，则时间会按照美国时间区算（UTC）
>
> ![image-20210513171231294](E:\images\image-20210513171231294.png)
>
> 这样会导致时间错乱

在setting中进行设置

```
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False
```

别忘了要在项目下的init下导包

```
import pymysql

pymysql.install_as_MySQLdb()
```

关于INSTALLED_APPS

![image-20210512140540877](E:\images\image-20210512140540877.png)

然后执行migrate命令

> 关于migrate
>
> migrate命令用于检查在INSTALLED_APPS中的设置，为其中的每一个app都创建一个数据表，用于迁移数据库

```
python manage.py migrate
```

随后创建模式

*这里有个小插曲*

如果说数据库在之前就创建好了，就需要用一个叫`inspectdb`的工具自动生成对应模型

[官方给的文档](https://docs.djangoproject.com/zh-hans/3.2/howto/legacy-databases/)

如果是手动创建模型

*这里暂时略过*

> 关于自动添加时间
>
> ```python
>     create_time = models.DateTimeField(blank=True, null=True,auto_now_add=True)
>     update_time = models.DateTimeField(blank=True, null=True,auto_now=True)
> ```
>
> 创建记录时需要添加auto_now_add
> 更改记录时需要添加auto_now

当经过各种操作生成了一个models.py的文件后，可以将文件（内容）迁移到指定应用的models下

![image-20210512154218055](E:\images\image-20210512154218055.png)

然后执行一次迁移 migrate

当模型创建并同步好后，就需要将模型激活

step1：要先将对应的应用的设置添加到setting的`INSTALLED_APPS`中，这代表该项目会包含该polls应用

![image-20210512154718628](E:\images\image-20210512154718628.png)

step2：其次运行makemigrations的命令，用于对刚刚修改的部分存储为一次迁移

```
python manage.py makemigrations polls
```

运行结果：

![image-20210512155125315](E:\images\image-20210512155125315.png)

> 关于迁移的定义
>
> 迁移是Django对数据库结构，也就是模型的定义变化的存储形式，就是磁盘上的文件，一般是可以阅读到的（如上面的呢个0001_initial.py文件）。

改变模型的三步

![image-20210512155842138](E:\images\image-20210512155842138.png)

*这里的概念还不是很熟悉，要多做几次实践*

当模型连接成功后就需要用用到数据库API来操纵数据库，先打开命令行

```
python manage.py shell
```

导入刚刚创建的模型

```
from polls.models import Friendtable,UserInfo
```

然后输入获取对象指令

```
UserInfo.objects.all()
```

结果：

![image-20210512161458083](E:\images\image-20210512161458083.png)

如果在models中添加上对应函数，则会返回实际值：

```
def __str__(self) -> str:
	return self.uemail
```

然后再重新进入并执行：

![image-20210512161625567](E:\images\image-20210512161625567.png)

**在外面加了数据后再重新执行，新的结果会立马程呈现**

*这里还有一些别的指令如增删改等等，先暂时略过*

# Django的管理界面

Django根据模型全自动生成后台界面

这是专门为管理者准备的

想要访问到管理后台需要创建一个可以登录管理页面的用户

```
python manage.py createsuperuser
```

然后就是一系列的输入用户名输入密码

![image-20210512163232925](E:\images\image-20210512163232925.png)

随后启动项目，登录到网站的`admin` 下

![image-20210512163345002](E:\images\image-20210512163345002.png)

此时的页面应该是没有我们添加的两个数据表，这个时候就要在admin.py中注册我们的数据表模型：

```
from .models import UserInfo,FriendTable

admin.site.register(UserInfo)
admin.site.register(FriendTable)
```

![image-20210512163530765](E:\images\image-20210512163530765.png)

然后再访问页面

![image-20210512163615804](E:\images\image-20210512163615804.png)

随后就可以进入到其中去对数据库里的数据做手动的管理了

![image-20210512163654556](E:\images\image-20210512163654556.png)

# 视图概念

