
str = "abcde"
str_2 = "fghij"

print("in操作符：","a" in str,"h" in str)
print("not in操作符：","a" not in str,"h" not in str)

print("序列连接操作",str+str_2)
print("序列重复操作",str*3)

tuple1 = (1,20)
tuple2 = (12,0)
# 返回True
print(tuple2 > tuple1)