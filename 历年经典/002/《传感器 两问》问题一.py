# Author: Su

'''
下面所示为一套由公司职员随身佩戴的位置传感器采集的数据,文件名称为"sensor.txt",其内容示
例如下:
2016/5/31 0:05, vawelon1,1,1
2016/5/31 0:20, earpa001,1,1
2016/5/31 2:26, earpa001,1,6
...(略)
第一列是传感器获取数据的时间,第二列是传感器的编号,第三列是是传感器所在的楼层,第四列是传感
器所在的位置区域编号。
问题一(10分):在右侧模板中修改代码,读入sensor.txt又文件中的数据,提取出传感器编号为
earpa001的所有数据,将结果输出保存到"earpa001.txt"文件。输出文件格式要求:原数据文件中
的每行纪录写入新文件中,行尾无空格,无空行。
参考格式如下:
2016/5/31 7:11, earpa001,2,4
2016/5/31 8:02, earpa001,3,4
2016/5/31 9:22, earpa001,3,4
...(略)
'''

# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

with open("sensor.txt",'r',encoding="utf-8") as f:
    lines = f.readlines()
with open("earpa001.txt",'w',encoding="utf-8") as fo:
    for line in lines:
        if "earpa001" in line:
            fo.write(line)

