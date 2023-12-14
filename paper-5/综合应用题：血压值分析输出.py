# Author: Su
'''
老王的女儿给老王测血压,在文件xueyajilu.txt中记录了一段时间的血压测量值。文件中每行是一条
记录,包含5个值:测量时间、左臂高压值、左臂低压值、右臂高压值、右臂低压值,每个字段用英文
逗号隔开,示例格式如下:
2018/7/2 6:00,140,82,136,90
2018/7/2 15:28,154,88,155,85
2018/7/3 6:30,131,82,139,74
2018/7/3 16:49,145,84,139,85
2018/7/4 5:03,152,87,131,85
......
使用字典和列表类型进行数据分析,输出老王的
左臂和右臂的高压最大值、低压最大值
左臂和右臂的高-低压差平均值
左臂和右臂的高压平均值、低压平均值
请注意每行三列对齐。输出的整数向下取整。
示例1:

'''
# 在…处填写多行代码
# 在_____出填写一行代码
# 可以修改其他代码
jl = [[], [], [], [], []]  # 1:zb_h, zb_l,yb_h,yb_l
zyc = []
yyc = []
with open("xueyajilu.txt", 'r', encoding='utf-8') as fi:
    for l in fi:
        lls = l.split(',')
        jl[0].append(int(lls[1]))
        jl[1].append(int(lls[2]))
        jl[2].append(int(lls[3]))
        jl[3].append(int(lls[4]))
        zyc.append(eval(lls[1]) - eval(lls[2]))
        yyc.append(eval(lls[3]) - eval(lls[4]))

cnt = len(zyc)
res = []
res.append(list(("高压最大值", max(jl[0]),max(jl[2]))))
res.append(list(("低压最大值", max(jl[1]),max(jl[3]))))
res.append(list(("压差平均值", sum(zyc)//cnt,sum(yyc)//cnt)))
res.append(list(("高压平均值", sum(jl[0])//cnt,sum(jl[2])//cnt)))
res.append(list(("低压平均值", sum(jl[1])//cnt,sum(jl[3])//cnt)))

print('{:<10}{:<10}{:<10}'.format("对比项", "左臂", "右臂"))
for r in range(len(res)):
    print('{:<10}{:<10}{:<10}'.format(res[r][0],res[r][1],res[r][2]))

