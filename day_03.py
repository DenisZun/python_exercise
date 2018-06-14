# encoding: utf-8

# 瀑布式开发
# 迭代式开发
# 敏捷式开发

# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。

# my answer
lis = []

for _ in xrange(3):
    num = int(raw_input("Please put a number:"))
    lis.append(num)

lis = sorted(lis)
lis_01 = [str(x) for x in lis]
print ','.join(lis_01)


# brand answer
# 冒泡排序
def bubble(list):
    n = len(list)
    for i in xrange(1, n):
        for j in xrange(1, n - i + 1):
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]

    lis_03 = [str(x) for x in list]
    return ','.join(lis_03)


if __name__ == '__main__':
    lis_02 = [12, 43, 54, 43, 65, 12, 31, 14]
    print bubble(lis_02)


# 题目：斐波那契数列。
# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，
# 指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。


# 方法1.生成器,关键字yield
def Fib(n):
    num1, num2 = 0, 1
    for _ in xrange(n):
        num1, num2 = num2, num1+num2
        yield num1

for i in Fib(10):
    print i


# 方法2.迭代器
class Fib(object):
    def __init__(self, n):
        self.n     = n
        self.index = 0
        self.num1  = 0
        self.num2  = 1

    def __next__(self):
        if self.index < self.n:
            num = self.num1
            self.num1, self.num2 = self.num2, self.num1+self.num2
            self.index += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    fib = Fib(10)
    for i in fib:
        print i


# 方法3(特殊方法).使用递归
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1)+fib(n-2)
print fib(10)


# 方法4(特殊方法).缓存
# 注意lru_cache为python3中才特有的缓存功能
import functools
from clockdeco import clock

@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__=='__main__':
    print(fibonacci(10))


