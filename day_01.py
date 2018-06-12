# encoding: utf-8
"""
一.
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
"""
import pprint  # pprint美观打印

# my_answer:

lis_01 = []


def func():
    lis = [1, 2, 3, 4]
    for i in lis:
        for j in lis:
            for k in lis:
                if (i != j) and (i != k) and (j != k):
                    num = i * 100 + j * 10 + k
                    lis_01.append(num)
    return lis_01

if __name__ == '__main__':
    # print func()
    pprint.pprint(func())


# standard method

list_num = ["1", "2", "3", "4"]
list_ret = []

def func():
    for i in list_num:
        for j in list_num:
            for k in list_num:
                if len(set(i + j + k)) == 3:
                    num = i + j + k
                    num = int(num)
                    list_ret.append(num)
    return list_ret
if __name__ == '__main__':
    pprint.pprint(func())


# special method

from itertools import permutations
list_nums = [1, 2, 3, 4]

# for i in permutations(list_nums, 3):
#     print i

for i in permutations([1, 2, 3, 4], 3):
    k = ''
    for j in range(0, len(i)):
        k = k + str(i[j])
    print (int(k))


"""
二.
企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？
"""
brand = [i*10**5 for i in range(11) if i % 2 == 0 and i != 8]
brand.reverse() # reverse是一个没有返回值的函数
brand.insert(-1, 10**5)

percent = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]


def price(money):
    r = 0
    lis = []
    for idx in range(6):
        if money>brand[idx]:
            r+=(money-brand[idx])*percent[idx]
            lis.append(r)
            money=brand[idx]
    return lis

if __name__ == '__main__':
    price(10**6)

# for i in range(len(brand)):
#     print brand[i]
