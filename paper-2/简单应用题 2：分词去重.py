# Author: Su
'''
参考编程模板,完善代码,实现以下功能。
利用jieba库实现中文分词。对分词后的列表进行去重处理,然后将务分词结果中字符数大于等于3的词
语,按照字符顺序排序,写入到文件out1.txt文件中。
out1.txt文件中每一行是分词后的一个词语。形式如下所示:
二十一
美国麻省理工学院
语言学
形象思维
突破性
总的来说
思维科学
软硬件
尼尔逊
温斯顿
机器人
'''

# 请在...处使用多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

...  #此处可多行
#对数据进行中文分词处理
import jieba
f = open('out1.txt','w')
fi = open("data.txt","r",encoding="utf-8")
lst = jieba.lcut(fi.read())
s = set(lst) #去重
s1 = sorted(s)
ls = list(s1) #集合重新变成列表
for item in ls:
    if len(item) >=3:
        f.write(item + "\n")
fi.close()
f.close()
