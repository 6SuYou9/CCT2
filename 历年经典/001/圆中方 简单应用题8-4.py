# Author: Su
'''
描述
使用turtle库的turtle.fd()函数和turtle.left()函数绘制一个边长为2200像素的正方形及一个紧挨四个顶
点的圆形,写入代码替换模板中的横线,不得修改其他代码,效果如图
'''

# 请在______处使用一行或多行代码替换
# 注意：请不要修改其他已给出代码
#该题系统无法图形识别，评阅默认正确，请自己核对答案。
#PY201.py
import turtle
turtle.pensize(2)
for i in range(4):
    turtle.fd(200)
    turtle.left(90)
turtle.left(-45)
turtle.circle(100*pow(2,0.5))