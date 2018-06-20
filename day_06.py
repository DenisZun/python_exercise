# encoding: utf-8
# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，
# 60-89分之间的用B表示，60分以下的用C表示。
# 程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。


def grade(n):
    arr = [90, 60, 0]
    grades_lis = ['A', 'B', 'C']

    for i in range(0, 3):
        if n >= arr[i]:
            grades = grades_lis[i]
            return grades

print grade(30)


# 题目：输出指定格式的日期
# 这种问题死记硬背

import time
import datetime

print time.time()
print time.localtime()
print time.asctime()
print time.strftime("%Y-%m-%d %H:%M:%S")

print datetime.datetime.now()
print datetime.date.today()
print datetime.date.today().strftime("%Y-%m-%d")
print datetime.date(2018, 6, 20)


# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

# method 1
import re
str = raw_input("请输入一个数:")

r1 = re.compile(r"[a-zA-Z]")
r2 = re.compile(r"[0-9]")
r3 = re.compile(r"\s+")

str_num = re.findall(r1, str)
print "字符类型个数为:{}".format(len(str_num))

digital_num = re.findall(r2, str)
print "数字类型个数为:{}".format(len(digital_num))

space_num = re.findall(r3, str)
print "空白字符类型个数为:{}".format(len(space_num))

others = len(str) - len(str_num) - len(digital_num) - len(space_num)
print "其他字符类型个数为:{}".format(others)


# method 2
str = raw_input("请输入一个字符串:")
length =  len(str)

list = [0, 0, 0, 0]

temp = [
    lambda i: 1 if (i.isdigit()) else 0,
    lambda i: 1 if (i.isspace()) else 0,
    lambda i: 1 if (i.isalpha()) else 0
]

for i in str:
    list[0] += temp[0](i)
    list[1] += temp[1](i)
    list[2] += temp[2](i)
    list[3] = length - list[0] - list[1] - list[2]

print list