# encoding: utf-8

# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# 分析: x + 100 = n^2     x + 100 + 168 = m^2
# 168 = (m-n)*(m+n)
# 设 i=m-n j=m+n 则m为(i+j)/2 n为(j-i)/2
# i, j 同为偶数且i >= 2


# my code
for i in range(1,85):
    if 168 % i == 0:
        j = 168 / i
        if  i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0 :
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            # print(x)
            print "m为{}".format(m)
            print "n为{}".format(n)


# brand method
for i in range(1, 85):
    if 168 % i == 0:
        j = 168 / i
        if i > j:
            m = (i + j)/2
            n = (i - j)/2
            if (m+n) * (m-n) == 168:
                print n**2 - 100


# special method
x1 = map(lambda i:i**2 - 100, range(1, 85))
x2 = map(lambda i:i**2 -100 - 168, range(1, 85))

set_01 =  set(list(x1))
set_02 =  set(list(x2))

set_list = set_01 & set_02
print set_list


# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，
# 然后再加上5天即本年的第几天，
# 特殊情况，闰年且输入月份大于2时需考虑多加一天：

# year = int(raw_input("请输入年份:"))
# month = int(raw_input("请输入月份:"))
# day = int(raw_input("请输入日期:"))
#
#
# def cals_date(y, m, d):
#     month_dict = dict(big_month = [1, 3, 5, 7, 8, 10, 12], mid_month = 2, small_month = [4, 6, 9, 11])
#
#     if (m in month_dict['big_month'] and d > 31) or (m in month_dict["small_month"] and d > 30):
#         print("invalid date")
#         return
#
#     month_list = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
#
#     if 0< m <= 12:
#         sum = month_list[m - 1]
#     else:
#         print "invalid date"
#         return
#     sum += d
#
#     if (y % 400 == 0) or (y % 4 == 0):
#         leap = 1
#
#         if m == 2 and d > 29:
#             print "invalid date"
#             return
#
#         if not leap and m == 2 and d not in range(1, 29):
#             print "invalid date"
#             return
#
#         if (leap == 1) and m > 2:
#             sum += 1
#     return 'it is the %dth day.' % sum
#
# print cals_date(year, month, day)



# brand method

import time

a = raw_input("输入时间（格式如：2017-04-04）:")
t = time.strptime(a,"%Y-%m-%d")
print t
print time.strftime('%j', t)
# print time.strftime("今年的第%j天",t).decode('utf-8')