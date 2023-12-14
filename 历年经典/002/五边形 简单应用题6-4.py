# Author: Su

'''
描述
使用turtle库的turtle.fd(函数和turtle.seth(函数绘制一个边长为100的正五边形,在模板中删除横线替换代码,不得修改其他代码。
效果如下图所示。
'''


# 请在______处使用一行或多行代码替换
#
# 注意：请不要修改其他已给出代码

import turtle
turtle.pensize(2)
d = 0
for i in range(1, 6):
    turtle.fd(100)
    d += 72
    turtle.seth(d)