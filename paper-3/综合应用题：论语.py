# Author: Su
'''
附件中有2个Python源文件和3个文本文件,分别对应两个问,题,请参考编程模板的py文件,修改
其中代码,实现以下功能:《论语》是儒家学派的经典著作之一,主要记录了孔子及其弟子言行。这
里给出了一个网络版本的《论语》,文件名称为"论语.txt",其内容采用逐句"原文"与逐句"注
释"相结合的形式组织,通过【原文】标记《论语》原文内容,过通过【注释】标记《论语》注释内容,
具体文件格式框架请参考"论语.txt"文件。(本题共计2问,本地回答第一问)
问题1:在PY301-1.py文件中修改代码,提取"论语.txt"文件中中的原文内容,输出保存到考生文件夹
下,文件名为"论语-原文.txt"。具体要求:仅保留"论语语.txt"文件中所有【原文】标签下面的内
容,不保留标签,并去掉每行行首空格及行尾空格,无空行。原文文小括号及内部数字是源文件中注释项
的标记,请保留。示例输出文件格式请参考"论语-原文-输出示例列.txt"文件。注意:示例输出文件仅
帮助了解输出格式,不作它用。
问题2:在PY301-2.py文件中修改代码,对"论语-原文.txt"或"论语.txt"文件进一步提纯,去掉每
行文字中所有小括号及内部数字,保存为"论文-提纯原文.txt"文文件。示例输出文件格式请参考"论
语-提纯原文-输出示例.txt"文件。注意:示例输出文件仅帮助了解输出格式,不作它用。
提示:建议使用Python集成开发环境IDLE编写、调试及验证程序
'''


# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准


fi = open("论语.txt", "r",encoding="utf-8")
fo = open("论语-原文.txt", "w",encoding="utf-8")
flag = 0
for line in fi:
    if "原文" in line:
        flag = 1
        continue
    elif "注释" in line:
        flag = 0
        continue
    if flag == 1:
        if line.strip():
            fo.write(line.strip()+'\n')
fi.close()
fo.close()

