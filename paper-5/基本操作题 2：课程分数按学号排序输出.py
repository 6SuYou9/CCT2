# Author: Su
'''
有一个列表studs如下:
studs= [{'sid':'103',Chinese': 90},
{'sid':'101','Chinese': 80},
{'sid':'102', Chinese': 70}]
将列表studs的数据内容提取出来,在屏幕上按学号从小到刂大的顺序显示输出每个学号对应的课程的
分数,格式见输出示例。
示例1:
输入:"无"
输出:
101:80
102:70
103:90
注意:请利用本地IDLE完善代码,编程调试至正确代码,并将编好的程序提交系统,得到评测结果。
'''
# 在_____处填写一行代码
# 不得修改其他代码

studs= [{'sid':'103','Chinese': 90},{'sid':'101','Chinese': 80},{'sid':'102','Chinese': 70}]
scores = {}
for stud in studs:
    sv = stud.items()
    for it in sv:
        if it[0] =='sid':
            k = it[1]
        else:
            scores[k] = it[1]
so = list(scores.items())
so.sort(key = lambda x:x[0],reverse = False)
for l in so:
    print('{}:{}'.format(l[0],l[1]))

