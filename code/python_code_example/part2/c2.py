# JSON
# 是一种轻量级的数据交换格式（数据格式）
# 字符串是JSON的表现形式
# 符合JSON格式的字符串 == JSON字符串
# 易于阅读
# 易于解析
# 网络传输效率高
# 跨语言交换数据

import json

json_str = '[{"name":"thirtyseven","age":18,"flag":false},{"name":"ioomie","age":19,"flag":true}]'

# 反序列化 JSON数据类型转换为python数据类型(并非只有json有这种说法)
# 序列号 python数据类型转换为JSON数据类型
print(json.loads(json_str))
'''
    json    python
    object  dict
    array   list
    string  str
    number  int
    number  float
    true    True
    false   False
    null    None
'''

# noSQL数据库 实现对象存贮
student = [
    {'name':"thirtyseven","age":18},
    {'name':"ioomie","age":19}
]
json_one = json.dumps(student)
print(json_one)

# JSON 数据格式
# JSON对象 无JSON对像说法，范畴在于js中
# JSON字符串 符合JSON格式的字符串 == JSON字符串