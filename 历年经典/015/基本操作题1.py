# Author: Su
'''
让用户输入一个符号作为填充字符,将"PYTHON"字符串以30字符宽、居中、其余部分以填充字符的
形式格式化输出。
示例如下(其中数据仅用于示意)
输入:#
输出:###########PYTHON##############
'''

#
# 编写代码替换横线
#

a = input("")  #请输入填充符号，例如：#
s = "PYTHON"
print("{:}".format(s.center(30,a)))