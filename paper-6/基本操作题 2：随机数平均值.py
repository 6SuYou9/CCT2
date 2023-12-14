# Author: Su
'''
输入一个正整数n,自动生成n个1-100范围内的随机浮点数,在屏幕上显示输出每个随机数,并显
示平均值。
要求:每行显示一个数据,小数点后保留2位。

示例1:
输入: "4"
输出: "
14.30
84.90
76.61
26.25
The average is:
50.52
"
'''

#在_____处填写一行代码
#不允许修改其他代码

import random
random.seed(1)
n = eval(input())
sum = 0
for i in range(n):
    fl = random.uniform(1,100)
    sum += fl
    print('{:.2f}'.format(fl))
print('The average is:{:.2f}'.format(sum/n))

