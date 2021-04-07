
# 没有加模式默认以只读的方式打开
# 当没有这个文件的时候会在同一级别的目录下生成该目录
file1 = open("name.txt","w")
file1.write("小明")
file1.close()

# 读文件
file2 = open("name.txt","r")
print(file2.read())
file2.close()

# 以追加的方式打开
# 如果以w的方式打开会将先前的内容进行覆盖
file3 = open("name.txt","a")
file3.write("\n小红")
file3.write("\n小星")
file3.close()

# 读取单行
file4 = open("name.txt","r")
print(file4.readline())
file4.close()

# 读取多行
file5 = open("name.txt","r")
for line in file5.readlines():
    print(line)
    # print("-------")
file5.close()

# 文件指针
file6 = open("name.txt","r")
print("当前文件指针：",file6.tell())
# 中文字符一个占两个偏移量
print(file6.read(1))
print("当前文件指针：",file6.tell())
# 将指针移动至开头
# 可以单独写seek(0)
# 第一个参数指偏移量 第二个参数有三种情况 0表示从头开始偏移，1表示从当前位置开始偏移，2表示从末尾开始偏移
file6.seek(0,0)
print("当前文件指针：",file6.tell())
file6.close()

