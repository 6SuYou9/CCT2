# Author: Su
members = {'张三':['人力部',5500],
            '李四':['后勤部',4500],
            '王三':['市场部',6500],
            '赵六':['开发部',8500]
           }
sal_dep = {}
max_val = 0
max_name = ""
for key in members:
    print('{}的工资是:{}, 部门是{}'.format(key,members[key][1],members[key][0]))
    if members[key][1]>max_val:
        max_val =  members[key][1]
        max_name = members[key][0]

print('工资最高的部门是:{},该部门工资是:{}'.format(max_name,max_val))

# 要点：
#
# 字典 members 里的 value 是个列表，所以需要用到列表的索引
# 对着字典 members 遍历，按照要求显示每个员工的工资和部门信息，另外还要取得工资和部门的名称存入字典 sal_dep
# 为了统计工资最高的部门的工资，需要字典 sal_dep 来保存这两个信息并且这个字典的 key 应该是工资数
# 用 max 函数对字典 sal_dep 的 key 进行求最大值的计算，并将最大值赋给变量 max_val
# 再从字典里，取出 key 为 max_val 的 value 赋给变量 max_name
# 最后按照要求显示结果
# 标准答案如下
members = {'张三':['人力部',5500],
            '李四':['后勤部',4500],
            '王三':['市场部',6500],
            '赵六':['开发部',8500]
           }
sal_dep = {}
for key in members:
    print('{}的工资是:{}, 部门是{}'.format(key, members[key][1], members[key][0]))
    sal_dep[members[key][1]] = members[key][0]
max_val = max(sal_dep)
max_name = sal_dep[max_val]
print('工资最高的部门是:{},该部门工资是:{}'.format(max_name,max_val))