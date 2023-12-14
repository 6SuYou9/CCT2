# Author: Su
score = [[87,79,90],[99,83,93],[90,75,89],[89,87,94],[95,85,84]]
for i in range(5):
    team = score[i]
    final = team[0]*0.6 + team[1]*0.3 + team[2]*0.1
    print('the {} final score is {}'.format(i+1, int(final)))

# 要点：
#
# 列表里每一个元素又是一个列表，对应一组的竞赛成绩
# 利用 len(score) 求得总的组数；
# 为了在输出语句里输出各组的编号数，所以需要使用带循环变量 i 的 for 循环
# 在这个循环结构中，按照计算公式计算每一组的总成绩，并显示输出计算结果
# 因为结果要求显示整数，格式定义里使用了int(final)。