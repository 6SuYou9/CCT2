# Author: Su
'''
使用字典和列表型变量完成村长选举。某村有40名有选举权和被选举权的村民,名单在附件name.txt
中,从这40名村民中选出一人当村长,40人的投票信息由附件vote.txt中给出,每行是一张选票的信
息,有效票中得票最多的村民当选。
问题:给出当选村长的名字及其得票数。
'''

'''

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
        D[vote[:-1]] = D.get(vote[:-1],0) + 1
        NUM+=1
l=list(D.items())
l.sort(key=lambda s:s[1],reverse=True)
name= l[0][0]
score=l[0][1]
print("有效票数为：{} 当选村民为:{}，票数为：{}".format(NUM, name, score))