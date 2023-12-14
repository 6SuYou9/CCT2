# Author: Su
'''
问题2:在PY301-2.py文件中修改代码,对"论语-原文.txt"或"论语.txt"文件进一步提纯,去掉每
行文字中所有小括号及内部数字,保存为"论文-提纯原文.txt"文件。示例输出文件格式请参考"论
语-提纯原文-输出示例.txt"文件。注意:示例输出文件仅帮助了解输出格式,不作它用。

'''

# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准


fi = open("论语-原文.txt", "r",encoding="utf-8")
fo = open("论语-提纯原文.txt", "w",encoding="utf-8")
# str1 = '123456789()'
# for line in fi:
#     for i in line:
#         if i in str1:
#             line=line.replace(i,"")
#     fo.write(line)
for line in fi:
    for k in range(100):
        line=line.replace('(' + str(k) + ')', '')
    fo.write(line)

fi.close()
fo.close()
