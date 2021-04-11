import os

# 绝对路径获取
print(os.path.abspath("."))
print(os.path.abspath(".."))

from pathlib import Path

p = Path("./testfolder")
# 创建文件夹
p.mkdir(parents=True)
# 删除文件夹
p.rmdir()
