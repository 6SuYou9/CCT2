# Author: Su
'''
键盘输入某班各个同学就业的行业名称,行业名称之间用空格间隔(回车结束输入)。完善Python代
码,统计各行业就业的学生数量,按数量从高到低方式输出。
示例1:
输入:"计算机 金融 计算机 建筑 土木 土木 "
输出:"
计算机:2
土木:2
金融:1
建筑:1
'''
# -*- coding:utf-8 -*-
'''
This is a python123.io file.
'''
#请在...上完善代码
names = input("")
t = names.split()
d = {} #定义一个字典
for c in range(len(t)): #对列表t中每一个元素统计出现次数
    d[t[c]] = d.get(t[c],0)+1  #要掌握字典get方法的具体使用，详见代码后面。
ls = list(d.items()) #将字典的items()转换为列表，形如[("计算机"，3),...]
ls.sort(key=lambda x:x[1], reverse=True) # 按照数量排序
for k in range(len(ls)):  #输出排序后的统计结果
    zy,num = ls[k]
    #例如：ls[0]=("计算机"，3),执行完该语句后，zy="计算机"，num = 3
    print("{}:{}".format(zy,num))#按照格式输出结果