# Author: Su

'''
问题二(10分):在右侧模板中修改代码,读入"earpa001.txt"文文件中的数据,统计earpa001对应
的职员在各楼层和区域出现的次数,保存到"earpa001_count.txt"文件,每一条纪录一行,位置信
息和出现的次数之间用英文半角逗号隔开,行尾无空格,无空行。参考格式如下。
1-1,5
1-4,3
...(略)
含义如下:
第1行"1-1,5"中1-1表示1楼1号区域,5表示出现5次;
第2行"1-4,3"中1-4表示1楼4号区域,3表示出现3次;
'''


# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

with open("earpa001.txt",'r',encoding="utf-8") as f:
    lines = f.readlines()
d = {}
for line in lines:
    li = line.strip(" \n").split(",")
    key = li[-2] + "-" + li[-1]
    d[key] = d.get(key,0) + 1
ls = list(d.items())
ls.sort(key=lambda x:x[1], reverse=True) # 该语句用于排序
with open("earpa001_count.txt",'w',encoding="utf-8") as fo:
    for i in ls:
        fo.write('{},{}\n'.format(i[0],str(i[1])))
