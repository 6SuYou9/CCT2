# Author: Su

'''
附件中有素材文件data3.txt,文件内容示例如下:
商业模式价值链由三个环节组成:产品、工具、社区。我们团队以一站式系统开发为当前主要产品,利
用XAMPP,PHPSTORM,微信开发者工具等软件根据客户要求提是供合适的一体化管理系统。
...(略)
请编程实现如下功能:
(1)统计文件中出现词频最多的前10个长度不小于2个字符的词语,将词语及其出现的词频数按照词频数
递减排序后显示在屏幕上,每行显示一个词语,用英文冒号连接词词语及其词频。
示例如下:
我们:5
系统:3
微信:3
...(略)
'''


#
# 请在此文件作答
#
import jieba
dict_words = {}
with open('data3-1.txt', 'r', encoding='GBK') as f:
    data = f.read()
ls = jieba.lcut(data)
for i in ls:
    if len(i)>=2:
        dict_words[i] = dict_words.get(i,0) + 1
ls = list(dict_words.items())
ls.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    print("{}:{}".format(ls[i][0],ls[i][1]))
