#  actor：dushaoduo
#  date:  2020.07.08

def canshu(name, age=23, *family, **friend):
    print(name)
    print(age)
    print(family)
    print(friend)
canshu("张三", 23, "父亲", "母亲", '111',a="李四", B="王五")

def Bl(num):
    print(num)
    if num > 0:
        return Bl(num-1)
        return Bl(num-1)
Bl(5)
