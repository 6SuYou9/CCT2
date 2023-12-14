# Author: Su
'''
使用turtle库的turtle.fd()函数和turtle.seth()函数绘制一个边长为40像素的正12边型,参考编程
模板,在横线处补充代码,不得修改其它代码。效果如下图所示。

'''

# 请在______完善代码,删除横线。
# 最后请用Print 输出你的结果，供系统评分。
import turtle
turtle.pensize(2)
d=0
for i in range(1,13):
    turtle.fd(40)
    d += 30
    turtle.seth(d)