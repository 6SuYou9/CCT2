# Author: Su


#问题1模板
#P301-1.py
#请在..........处填写多行表达式或语句
#可以修改其他代码


picd = {}
fi = open("dir_50.txt",'r')
for l in fi:
    l = l.strip()
    if len(l):
        lkey = l.split("_")[1][:-4]
        ls = eval(l.split("_")[0])
        lval = [int(num) for num in ls if num != "0" ]
        picd[lkey] = lval
fi.close()
print(picd)
idd = {}
for key in picd:
    for i in picd[key]:
        idd[str(i)] = idd.get(str(i),0) + 1
s = 0
print(idd)
for key in idd:
    s += idd[key]
count = len(idd)
print("实际参加测试的人数是：{}".format(count))
print("人均被测次数是：{:.1f}".format(s/count))



