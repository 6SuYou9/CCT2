# Author: Su
'''
使用turtle库的函数绘制10层螺旋状放大的类正方形,类正方形边长从0度方向、边长为1像素开
始,每条边长度比前一条边增加2个像素,画笔逆时针旋转91度。效果如下图所示。

'''

import turtle
d = 0
k = 1
for j in range(10):
   for i in range(4):
       turtle.fd(k)
       d += 91
       turtle.seth(d)
       k += 2
turtle.done()
