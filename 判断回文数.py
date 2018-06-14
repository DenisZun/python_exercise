# encoding: utf-8

"""
回文数:
In [7]: a
Out[7]: 'helloworlddlrowolleh'

In [8]: a[::-1]
Out[8]: 'helloworlddlrowolleh'

In [9]: a == a[::-1]
Out[9]: True
"""


def is_palindrome(num):
    temp = "%d" % num
    return temp == temp[::-1]


def create_palindrome(num):
    """判断是否回文数,是就返回不是就创建"""
    count = 0
    while True:
        num = int(num)
        if is_palindrome(num) == True:
            output = "这是一个回文数:%d"%num + "\r\n总共次数为%d"%count
            return output
        else:
            num = add(num)
            count += 1


def add(num):
    temp = "%d"%num
    str = temp[::-1]
    return temp + str

if __name__ == '__main__':
    print create_palindrome(34231412342342)


