# Author: Su

'''
使用turtle库和random库,绘制四个彩色的正方形,正方形颜色随机从颜色列表color中获取;
正方形边长从范围[50,200]之间选取,每个正方形左下角坐标x和y从范围[-100,100]之间选取。
'''

# 在____________上补充代码 （12根短线）
#
import random
import turtle as t
import random as r

color = ['red','blue','purple','black']
r.seed(1)
for j in range(4):
    t.pencolor(color[r.randint(0,3)])
    t.penup()
    t.goto(r.randint(-100,100),r.randint(-100,100))
    t.pendown()
    ra = r.randint(50, 200)
    for i in range(1,5):
        t.fd(ra)
        t.seth(90*i)
t.done()