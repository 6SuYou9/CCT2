# Author: Su
import random as r
zmb = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
r.seed(1)
code = ''
for i in range(4):
    code+=r.choice(zmb)

print(code)

#  要点
#
# 1.用随机数要导入random库，并记别名为r
#
# 2.先定义好要使用的英文字母表；
#
# 3.用seed（1）初始化随机函数，保证后面产生的随机数跟标准答案的一致
#
# 4.初始化密码code为一个空字符串；
#
# 5. 循环4次，在循环里构造验证码的每个字符。从英文字母表里随机选取一个字母；用字符串的+=运算符，追加到密码变量上。