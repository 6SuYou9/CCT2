# Author: Su
'''
从键盘上输入球的半径r,输出球的表面积 S 和体积 V (1个英英文空格隔开)
球体表面积是指球面所围成的几何体的面积,它包括球面和球面面所围成的空间。
示例1:
输入:"2"
输出:"50.24 33.49"
'''

#请在_____完善一行代码
PI = 3.14
r = eval(input())
S = 4*PI*r*r # 球体表面积
V = 4*PI*r*r*r/3  #球体体积
print("{:.2f} {:.2f}".format(S,V))