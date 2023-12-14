# Author: Su
'''
则A和B两点之间的距离为:
|AB| =(x1-x2)2+(у1-y2)2
请输入4个数字(用空格分隔),分别表示x1、y1、x2、y2,计算距离(保留2位小数输出)。
参考编程模板,参考输入输出示例,完善程序。
示例1:
输入:"1234"
输出:"2.83"
示例2:
输入:"1122"
输出:"1.14"
'''

ntxt = input("")
nls = ntxt.split(" ")
x1 = eval(nls[0])
y1 = eval(nls[1])
x2 = eval(nls[2])
y2 = eval(nls[3])
r = pow(pow(x2-x1, 2) + pow(y2-y1, 2),  0.5)
print("{:0.3}".format(r))
