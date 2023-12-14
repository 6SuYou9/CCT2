# Author: Su

'''
《命运》是著名科幻作家倪匡的作品。这里给出《命运》的一个网络本文件,文件名为"命运.txt"
问题一、(5分)在右侧修改代码,对"命运.txt"文件进行字符频次统计,输出频次最高的中文字符
(不包括标点符号)及其频次,字符与频次之间采用英文冒号":";分隔
示例格式如下:
理:224
'''

# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

dela = "，。："
with open("命运.txt",'r',encoding="utf-8") as f:
    text = f.read()
d = {}
for i in text:
    i = i.strip()
    if (i in dela) or i == "\n":
        continue
    d[i] = d.get(i,0) + 1

ls2 = list(d.items())
ls2.sort(key = lambda x:x[1],reverse=True)

print("{}:{}".format(ls2[0][0],ls2[0][1]),end="")
