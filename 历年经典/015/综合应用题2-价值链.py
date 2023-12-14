# Author: Su

'''
编程实现如下功能:
(2)将文档以中文逗号及中文句号为分隔符分割成短句,将包含最高词频的词语的句子,输出到文件out.
txt中,每句一行,示例如下:
以此为我们吸引更多的商机
同时普及我们的一站式开发技术
(略)
'''

import jieba
dict_words = {}
with open('data3.txt', 'r', encoding='GBK') as f:
    data = f.read()
ls = jieba.lcut(data)
for i in ls:
    if len(i)>=2:
        dict_words[i] = dict_words.get(i,0) + 1
ls = list(dict_words.items())
ls.sort(key=lambda x:x[1],reverse=True)
string = ls[0][0]

datas = data.replace("，","-").replace("。","-")
datas = datas.split("-")
print(datas)
with open("out.txt",'w') as f:
    for juzi in datas:
        juzi = juzi.strip()
        if string in juzi:
            f.write(juzi+"\n")
            print(juzi)