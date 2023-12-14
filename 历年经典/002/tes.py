# Author: Su


# while True:
#     guess =eval(input())
#     if guess == 0x452//2:
#         break
# print(guess)

fo = open("book.txt","w")
ls = ['book','23','201009','20']
fo.writelines(ls)
fo.close()
