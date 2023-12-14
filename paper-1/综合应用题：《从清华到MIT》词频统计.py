# Author: Su

# 标准答案如下
import jieba        # 导入jieba中文分词库
dk = {}             # 定义dk字典变量 type(dk):<class 'dict'>

#使用with后不管with中的代码出现什么错误，都会进行对当前对象进行清理工作。
#例如file的file.close()方法，无论with中出现任何错误，都会执行file.close()方法

#以指定utf-8编码只读方式打开data.txt文件，文件句柄命名为f
with open('data.txt','r',encoding = "utf-8") as f:
    sl = f.readlines()

#print(type(f))    f是<class '_io.TextIOWrapper'>文件句柄的类型
# print(type(sl))   # sl是一个列表，包含了文件中每一行内容
# print(sl)
# print(type(sl[0]))  # sl[0]是列表sl中第一个元素，是文件中第一行所有内容

for s in sl:        #循环读取列表元素
    k =jieba.lcut(s, cut_all = True)
    # print(k)    # 测试
    #对每个s,使用jieba.lcut函数以全模式方式返回一个列表(由词语组成）
    for wo in k:    #对每个词语进行筛选
        if len(wo) == 2:    #如果词语的长度为2,进行统计
           dk[wo] = dk.get(wo,0) + 1
           #逐步构建统计字典，形式如{"大学":1,"设计":2,...},备注，这里的1、2是逐渐变化中

# print(dk.items())
dp = list(dk.items())   #转换为列表，列表中元素为元组。
# print(dp)
dp.sort(key= lambda x:int(x[1]), reverse = True)

for i in range(10):   #输出排序后的内容
   print("{}:{}".format(dp[i][0],dp[i][1]))