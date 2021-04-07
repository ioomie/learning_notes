
# 列表推导式
alist = [i*i for i in  range(1,11) if i%2 == 0]

print(alist)

# 字典推导式
# 这在爬虫的时候会经常用到 如解析cookies
adict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three"
}
bdict = {key:value for key,value in adict.items()}
print(bdict)
