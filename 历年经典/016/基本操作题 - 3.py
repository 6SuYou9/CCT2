# Author: Su

'''
获得用户输入的三个整数,以逗号分隔,分别记为:n、m、k,其中m>k。
以1为随机数种子,产生n个在k和m之间的随机整数(包括k和m),将这些随机数输出,每个数一行。
示例如下(其中数据仅用于示意):
输入: 4,26,10
输出示例如下:
14
12
26
11
'''


# 请在......处完善代码，可以修改其他代码

import random as r
r.seed(1)
s=input("请输入三个整数 n,m,k：")
slist=s.split(",")
for i in range(eval(slist[0])):
    print(r.randint(eval(slist[2]),eval(slist[1])))

num_list = range(eval(slist[2]),eval(slist[1])+1)
for i in r.sample(num_list,eval(slist[0])):
    print(i)



