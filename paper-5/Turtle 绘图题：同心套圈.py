# Author: Su
'''
使用turtle库绘制四个同心圆套圈,最小的圆圈半径为10像素,不同圆圈之间的半径差是50像素,
效果如下图所示。

'''

# 请在______处补充一行代码
# 请不要修改其他代码
# 在IDLE运行时，请去掉代码注释部分。

import turtle
r = 10
dr = 50
head = 90
for i  in range (4):
    turtle.pendown()
    turtle.circle(r)
    r +=  dr
    turtle.penup()
    turtle.seth(-head)
    turtle.fd(dr)
    turtle.seth(0)
turtle.done()