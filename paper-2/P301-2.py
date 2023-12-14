# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

ls = []
with open("PY301-SunSign.csv",'r',encoding="utf-8") as f:
      for line in f.readlines():
            line = line.strip()
            ls.append(line.split(","))
while True:
      s = (input("请输入星座序号(例如,5 10):")).split(" ")
      for i in s:
            if eval(i)>12 or eval(i)<1:
                  print("输入星座序号有误！")
                  continue
            xingzuo = ls[eval(i)]
            print("{}({})的生日是{}月{}日至{}月{}日之间".format(xingzuo[1],xingzuo[4],xingzuo[2][0:-2],xingzuo[2][-2:],xingzuo[3][0:-2],xingzuo[3][-2:]))
