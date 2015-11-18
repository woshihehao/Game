
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, atk, blood):
        self.name = name
        self.atk = atk
        self.blood = blood

    def attack(self, b):
        hurt = b.blood if self.atk > b.blood else self.atk
        b.blood -= hurt
        print '%s攻击%s，%s收到%d点伤害，%s剩余生命值：%d' % (self.name, b.name, b.name, hurt, b.name, b.blood)


def Fight(a, b):
    flag = True
    while a.blood > 0 and b.blood > 0:
        if flag:
            a.attack(b)
        else:
            b.attack(a)
        flag = not flag
    if a.blood > 0:
        print "%s获胜" % (a.name)
    if b.blood > 0:
        print "%s获胜" % (b.name)


def main():
    per = []
    for i in range(2):
        name_ = raw_input('名字：')

        atk_ = input('攻击力：')
        blood_ = input('血量：')

        per.append(Student(name_, atk_, blood_))

    '''zhang_san = Student('张三', 2, 6, 2)
    li_si = Student('李四', 2, 7, 1)'''
    Fight(per[0], per[1])
if __name__ == "__main__":
    main()