# Author: Su

'''
《命运》是著名科幻作家倪匡的作品。这里给出《命运》的一个网络本文件,文件名为"命运.txt"
问题三、(10分)在右侧修改代码,对"命运.txt"文件进行字:符频次统计,将所有字符按照频次从高
到低排序,字符包括中文、标点、英文等符号,但不包含空格和回车。将排序后的字符及频次输出到考
生文件夹下,文件名为"命运-频次排序.txt"。字符与频次之间采用英文冒号":"分隔,各字符之间
采用英文逗号","分隔,参考CSV格式,最后无逗号
'''

# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

with open("命运.txt",'r',encoding="utf-8") as f:
    text = f.read()
d = {}
for i in text:
    i = i.strip("()")  # 这里是真不理解为什么，难道是()不算中英文符号？
    if (i == "\n") or (i == " "):
        continue
    d[i] = d.get(i,0) + 1

ls2 = list(d.items())
ls2.sort(key = lambda x:x[1],reverse=True)
string = ""
for i in ls2:
    if i != ls2[-1]:
        string += "{}:{},".format(i[0],i[1])
    else:
        string += "{}:{}".format(i[0], i[1])
with open("命运-频次排序.txt",'w',encoding="utf-8") as f:
    f.write(string)

