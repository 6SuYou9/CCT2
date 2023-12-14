# Author: Su

'''
描述
使用字典和列表型变量完成村长选举。某村有40名有选举权和被选举权的村民,名单在附件name.txt
中,从这40名村民中选出一人当村长,40人的投票信息由附件vote.txt中给出,每行是一张选票的信
息,有效票中得票最多的村民当选。
问题:请从vote.txt中筛选出无效票写入文件vote1.txt。有效票的含义是:选票中只有一个名字且该
名字在name.txt文件列表中,不是有效票的票称之为无效票。
'''

f=open("name.txt",encoding="utf-8")
names=f.readlines()
f.close()
f=open("vote.txt",encoding="utf-8")
votes=f.readlines()
f.close()
D={}
NUM=0
for vote in votes:
    num = len(vote.split())
    if num==1 and vote in names:
        D[vote[:-1]] = D.get(vote,0) + 1
        NUM+=1
    else:
        with open("vote1.txt","a+",encoding="utf-8") as fi:
            fi.write("{}".format(vote))