# Author: Su

'''
问题2:读取问题1输出的文件result301.txt,对确诊人数进行排序,输出确诊人数最多的地区名称和
人数。
示例如下(其中数据仅用于示意):
新冠确诊人数最多的国家是United States,人数是19000000
新冠确诊人数超过1W的国家有20个
新冠确诊人数为0的国家有40个
'''

#
# 在____________上补充代码 （12根短线）
# 在……上补充一行或多行代码 （6个点）
#
lcnum = []
with open("result301.txt", "r",encoding="utf-8") as fi:
    for line in fi:
        data = line.strip().split(":")
        data = [data[0].replace('"',""),int(data[1])]
        lcnum.append(data)
lcnum.sort(key=lambda x:x[1], reverse= True)
lz = 0
lw = 0
for l in lcnum:
    if l[1] == 0:
        lz += 1
    elif l[1]>10000:
        lw += 1

print("新冠确诊人数最多的国家是{},人数是{}".format(lcnum[0][0],lcnum[0][1] ))
print("新冠确诊人数超过1W的国家有{}个".format(lw))
print("新冠确诊人数为0的国家有{}个".format(lz))
