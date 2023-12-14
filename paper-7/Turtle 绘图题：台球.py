# Author: Su

'''
使用turtle库绘制下面的5行圆圈图案,第一行5个圆圈,向下逐行递减,第5行1个圆圈。圆圈居
中排列,半径为20像素。效果如下图所示。
'''

#在_____上填写一行代码

import turtle
def drawCircle():
    turtle.pendown()
    turtle.circle(20)
    turtle.up()
    turtle.fd(40)
def drawRowCircle(n):
    for j  in range(n,1,-1):
        for i in range(j):
            drawCircle()
        turtle.fd(-j*40-20)
        turtle.right(90)
        turtle.fd(40)
        turtle.left(90)
        turtle.fd(40)
    drawCircle()
drawRowCircle(5)
turtle.hideturtle()
turtle.done()