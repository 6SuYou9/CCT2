# Author: Su
'''
《命运》是著名科幻作家倪匡的作品。这里给出《命运》的一个网络本文件,文件名为"命运.txt"
问题二、(5分)在右侧编程模板中修改代码,对"命运.txt"文进行字符频次统计,按照频次由高到
低,在屏幕输出前10个频次最高的字符,不包含回车符,字符。之间无间隔,连续输出
示例格式如下:
理斯卫...(后略,共10个字符)
'''

# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

with open("命运.txt",'r',encoding="utf-8") as f:
    text = f.read()
d = {}
for i in text:
    i = i.strip()
    if i == "\n":
        continue
    d[i] = d.get(i,0) + 1

ls2 = list(d.items())
ls2.sort(key = lambda x:x[1],reverse=True)
for i in range(11):
    print(ls2[i][0],end="")
