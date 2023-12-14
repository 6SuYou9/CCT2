# Author: Su

'''
请参考编程,编写代码替换横线内容,不得修改其他代码,实现下面
功能。
(1)使用turtle库和random库,在屏幕上绘制5个彩色的圆;
(2)圆的颜色随机从颜色列表color中获取;
(3)圆的圆心坐标x和y值从范围[-100,100]之间选取,半径从范围[10,30]之间选取。
'''

#请在___横线上完善代码

import turtle as t
import random as r

color = ['red','green','blue','purple','black']
r.seed(1)
for j in range(5):
    t.pencolor(color[r.randint(0,4)])
    t.penup()
    t.goto(r.randint(-100,100),r.randint(-100,100))
    t.down()
    t.circle(r.randint(10,30))
t.done()