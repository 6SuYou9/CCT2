# Author: Su


'''
参考编程模板,删除横线,完善代码实现以下功能。
data1.txt文件保存了一组汉字,输出该文件不同汉字的数量。
示例如下(其中数据仅用于示意):
输出:100
'''

#
# 请完善代码
#

f = open('data1.txt','r',encoding="gbk")
ls = []
for line in f:
      for c in line:
            if (c not in ls) and c!="\n":
                  ls.append(c)
f.close()
print(len(ls))
