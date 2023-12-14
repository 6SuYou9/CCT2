# Author: Su

# a="3000"
#
# if a < 2000:
#     print("少")
# elif a > 4000:
#     print("不多")
# else:
#     print("还行")


# l1 = [1,2,3,4]
# st = ""
# for i in l1:
#     st += i
# print(st)

# ls = ["try"]  # 全局变量
#
#
# def mtry(lt):  # 形参
#     print(lt) # ['trt'] # 形参lt指向实参ls
#     lt.append(ls)  # 形参lt指向实参ls
#     print(lt)  # ['trt', ['try']] # 形参lt指向实参ls
#     return lt  # 返回形参lt
#
#
# print(mtry(mtry(["trt"])))

import time

print(time.localtime())