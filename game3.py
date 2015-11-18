# -*- coding: utf-8 -*-

__author__ = 'hehao'


class Student(object):
    def __init__(self, name_, atk_, blood_, defense_, role_):
        self.name = name_
        self.atk = atk_
        self.blood = blood_
        self.defense = defense_
        self.role = role_

    def attack(self, b):
        if b.defense <= self.atk:
            real_damage = self.atk - b.defense
            hurt = b.blood if real_damage > b.blood else real_damage
            b.blood = b.blood - hurt
            print '%s%s攻击%s，%s收到%d点伤害，%s剩余生命值：%d' % (self.role, self.name, b.name, b.name, hurt, b.name, b.blood)

        else:
            self.blood = 0
            print '连防御都破不了，打个卵'


def Fight(a, b):
    flag = True
    while a.blood > 0 and b.blood > 0:
        if flag:
            a.attack(b)
        else:
            b.attack(a)
        flag = not flag
    if a.blood > 0:
        print "%s%s获胜" % (a.role, a.name)
    if b.blood > 0:
        print "%s%s获胜" % (b.role, b.name)


def main():
    per = []
    for i in range(2):
        role_ = raw_input('职业：')

        name_ = raw_input('名字：')

        atk_ = input('攻击力：')
        blood_ = input('血量：')
        defense_ = input('防御力：')
        per.append(Student(name_, atk_, blood_, defense_, role_))


    '''zhang_san = Student('张三', 2, 6, 2)
    li_si = Student('李四', 2, 7, 1)'''
    Fight(per[0], per[1])

if __name__ == "__main__":
    main()
