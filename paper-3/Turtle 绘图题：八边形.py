# Author: Su

'''
绘制如下图所示八边形。八边形的边长为100。

'''
# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

import turtle
turtle.pensize(2)
d = 0
for i in range(1, 9):
    turtle.forward(100)
    d += 360/8
    turtle.seth(d)
