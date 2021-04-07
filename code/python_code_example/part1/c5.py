
# 异常
try:
    file = open("namb.txt")
except Exception as e:
    print("输出异常")
    print(e)
finally:
    print("不管如何都要将文件进行关闭")
    file.close()