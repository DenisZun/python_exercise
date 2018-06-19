# encoding: utf-8
# 题目：暂停一秒输出，并格式化当前时间。
# 格式化时间输出

import time, datetime

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
time.sleep(1)
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

time_01 = datetime.datetime.now()
print time_01.strftime("%Y-%m-%d %H:%M:%S")


# 题目：打印出所有的"水仙花数"，
# 所谓"水仙花数"是指一个三位数，
# 其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，
# 因为153=1的三次方＋5的三次方＋3的三次方。

def shuixian(n):
    lis = []
    for i in range(100, n):
        l = i / 100
        j = (i - l*100)/10
        k = i % 10
        if i == l ** 3 + j ** 3 + k ** 3:
            lis.append(i)
    return lis

for i in  shuixian(1000):
    print i


# 题目：将一个正整数分解质因数。
# 例如：输入90,打印出90=2*3*3*5。
def reduce_num(n):
    """分解质因式"""
    num =  '{} = '.format(n)

    if not isinstance(n, int):
        print "请输入一个整数"

    while n <> 1:
        for index in xrange(2, n+1):
            if n % index == 0:
                n /= index
                if n == 1:
                    print index
                else:
                    print  '{} * '.format(index),

reduce_num(90)

def reduce_num_01(n):
    """分解质因式"""
    l = []
    while n > 1:
        for i in xrange(2, n+1):
            if n % i == 0:
                n = int(n/i)
                l.append(i)
                break
    return l

lis_num = reduce_num_01(1909900)

i = 1
for a in lis_num:
    i *= a

num = "{}".format(str(i)) + "=" + "*".join(str(x) for x in lis_num)
print num


# 打印100到200之间的所有素数
from math import sqrt


def isprime():
    lis = range(100, 200)
    p = lis[:]

    for i in xrange(100, 200):
        for j in xrange(2, int(sqrt(i) + 1)):
            if i%j == 0:
                p.remove(i)
                break
    return p
print isprime()

lis_01 = list(filter(lambda x: x not in set([i for i in xrange(100, 200) for j in xrange(2, i) if not i%j]), range(100, 200)))
print lis_01