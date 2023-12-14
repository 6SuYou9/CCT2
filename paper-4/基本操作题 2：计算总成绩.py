# Author: Su
'''
参考编程模板,读取附件data.txt中的内容,计算第一行学生的总成绩,然后参考输入输出示例将结果
直接输出到窗口中。不得修改程序中已给出的框架内容。
特别提醒:如果同学们在IDLE中编程,请把.py文件和data.txt文件放在同一目录下。
示例1:
输入:无
输出:"314"
'''

#请在__________上补充完成一行代码
#不改变已有的编程框架内容
with open("data1.txt", "r", encoding="utf-8") as fi:
    line = fi.readline().split(',')
print(str(eval(line[1])+eval(line[2])+eval(line[3])))
