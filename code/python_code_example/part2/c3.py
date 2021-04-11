import time
import datetime
# 时间模块

print(time.time())
print(time.localtime())
print(time.strftime("%Y|%m|%d"))

# 获取当前时间
print(datetime.datetime.now())

# 修改时间偏移量
newtime = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + newtime)

# 获取某一天
oneday = datetime.datetime(2021,8,30)
newday = datetime.timedelta(days=10)
print(oneday+newday)