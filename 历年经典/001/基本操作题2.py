# Author: Su

'''
描述
请在模板中写代码替换横线,不修改其它代码,请实现以下功能DE:
随机选择手机品牌列表brandlist=['华为',苹果',诺基亚','OPPO',小米']中的一个手机品牌,屏幕输出。
'''

# 请在______处使用一行代码或表达式替换
#该模板仅是提示作用，你可以全部删除重新作答，输出一致即可正确得分。
#请删除横线， 不要在横线上作答。

import random
brandlist = ['华为','苹果','诺基亚','OPPO','小米']
random.seed(0)
name = random.choice(brandlist)
print(name)