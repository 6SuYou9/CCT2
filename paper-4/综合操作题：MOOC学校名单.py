# Author: Su
'''
附件文件data.txt是教育部爱课程网中国大学MOOC平台的某个HTML页面源文件,里面包含了我国参
与MOOC建设的一批大学或机构列表。
问题1:请编写程序,从data.txt中提取大学或机构名称列表,将结果写入文件univ.txt,每行一个大学
或机构名称,按照大学或机构在data.txt出现的先后顺序输出,样例如下:
...
南京理工大学
...
南京师范大学
...

提示:所有大学名称在data.txt文件中以 alt="南京理工大大学"形式存在。
问题2:请编写程序,从univ.txt文件中提取大学名称,大学名名称以出现"大学"或"学院"字样为参
考,但不包括"大学生"等字样,将所有大学名称在屏幕上输出出,大学各行之间没有空行,最后给出名
称中包含"大学"和"学院"的名称数量,同时包含"大学"和"学院"的名称以结尾的词作为其类
型。样例如下(样例中数量不是真实结果,北京工商大学嘉华学院算作学院):
...
南京理工大学
...
长沙师范学院
...
包含大学的名称数量是10
包含学院的名称数量是12

'''
#编程模板1：PY301-1.py
# 请在______处使用一行或多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

with open("data.txt","r",encoding="utf-8") as f:
    data = f.readlines()
f = open("univ.txt", "w")
for line in data:
    if "alt=" in line:
        dx = line.split("alt=")[-1].split('"')[1]
        f.write(dx+'\n')
f.close()

#编程模板2：PY301-2.py
# 请在______处使用一行或多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

n = 0
m = 0
f = open("univ.txt", "r")
lines = f.readlines()
f.close()
for line in lines:
    line = line.replace("\n","")
    if '大学生' in line:
        continue
    elif '学院' in line and '大学' in line:
        if line[-2:] == '学院':
            m += 1
        elif line[-2:] == '大学':
            n += 1
        print('{}'.format(line))
    elif '学院' in line:
        print('{}'.format(line))
        m += 1
    elif '大学' in line:
        print('{}'.format(line))
        n += 1
print("包含大学的名称数量是{}".format(n)) #输出大学计数
print("包含学院的名称数量是{}".format(m)) #输出学院计数
