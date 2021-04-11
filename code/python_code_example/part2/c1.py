import re

str1 = "ah3bud98cha83bx0cna9023hnfnxs0923ndf9sn390fhw9fcn390"

str2 = "abc,acc,adc,aec,afc,ahc,asdio,ahsdi,asnio,asdni"

# print(re.findall('\D',str1))
print(re.findall("a[cfd]c*", str2))
print(re.findall("a[^cfd]c*", str2))
print(re.findall("a[c-f]c*", str2))
print(re.findall("[A-Za-z0-9_]", str2))
print(re.findall("\w", str2))

# 空白字符
print(re.findall("\s", str2))

# 单词字符匹配3个
print(re.findall("\w{3}", str2))

# 默认情况为贪婪匹配
print(re.findall("\w{3,6}", str2))

# 非贪婪
print(re.findall("\w{3,6}?", str2))

# * 对前面的字符匹配0次或无限多次
# + 匹配1次或者无限多次
# ? 匹配0次或者1次
print(re.findall("\w+", str2))

# 边界匹配
number = '17101238,1368019,6239187,1207123,6806979,12367087,2187300808,123,1234,12334'
print(re.findall("\d{3},", number))
# print(re.findall("(1){3}",number))

# 忽略字母大小写
# re.S可以让.匹配换行符
print(re.findall("xxx", str2, re.I | re.S))

language = "PythonC#JavaC#PHPC#"
# 0表示一直替换
print(re.sub("C#", "GO", language, 0))
print(language.replace("C#", "GO"))


# re.sub的第二个参数可以是个函数传入

def trange(value):
    re_value = value.group()
    print(re_value)
    return "???" + re_value


print(re.sub("C#", trange, language))

s = "A8C3721D86"


def number_trange(value):
    re_value = int(value.group())
    if re_value >= 6:
        return "9"
    elif re_value < 6:
        return "0"


print(re.sub("\d", number_trange, s))

# match从字符串的首字母开始，若没找到就直接返回空
# re.match()
# search搜索整个字符串，找到第一个匹配成功并返回
# re.search()
# 返回的是对象
# 关于返回对象的方法
# r.span()返回结果所在字符串种的对象
# r.group()返回结果的值
# r.group(0)返回所有的的字符
# r.groop(1,2,3...)返回圆括号内括住的内容
# r.groups()返回所有组


# \d \D 数字 非数字
# \w \W 单词字符 [A-Za-z0-9_] 非单词字符集（包括空格）
# \s \S 空白字符 非空白字符
# . 匹配除换行符\n之外其他所有字符
