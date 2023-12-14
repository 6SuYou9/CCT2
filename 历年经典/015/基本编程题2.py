# Author: Su

'''
从键盘上获取一个由英文逗号、字母、汉字、数字字符组成的输入,计算该输入中所有数之和,并输
出。
示例如下(其中数据仅用于示意):
输入:1,海淀区,ab,56,3,中关村
输出:数字和是:60
'''

#
# 编写代码替换横线
#

myinput = input("") #请输入：
ls = myinput.split(",")
s = 0
for c in ls:
    if c.strip(" ").isdigit():
        s+=int(c)
print("数字和是：" + str(s))