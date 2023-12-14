# Author: Su
'''
使用中文分词jieba库,对下面的s字符串进行精确模式分词。将分词后得到的列表 1s输出到窗卤

s = "人工智能是包括十分广泛的科学，它由不同的领域组成，如机器学习，计算机视觉等等，总的说来，人工智能研究的一个主要目标是使机器能够胜任一些通常需要人类智能才能完成的复杂工作。但不同的时代、不同的人对这种“复杂工作”的理解是不同的。"

输入:无
输出:"["人工智能','是',包括',......]"

'''
#在______完善一行代码
import jieba
s ='''人工智能是包括十分广泛的科学，
它由不同的领域组成，如机器学习，计算机视觉等等，
总的说来，人工智能研究的一个主要目标是使机器能够胜任
一些通常需要人类智能才能完成的复杂工作。但不同的时代、
不同的人对这种“复杂工作”的理解是不同的。'''

ls = jieba.lcut(s)
print(ls)