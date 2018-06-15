# encoding: utf-8
# 题目：将一个列表的数据复制到另一个列表中。

import copy
a = [1, 2, 3]
b = [3, 4, 5]
c = [a, b]

# 浅拷贝
d = copy.copy(c)
print id(d[1])
print id(c[1]) == id(d[1])

# 深拷贝
e = copy.deepcopy(c)
print id(e[1])

# 等价于浅拷贝
f = c[:]
print id(f[1]) == id(d[1])

# 将列表拓展倒空列表中
lis = []
lis.extend(c)
print lis

# 补充点列表的操作不能边遍历边增删
list_demo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in list_demo:
   list_demo.remove(i)

# list_demo = [2, 4, 6, 8, 10]
# 原因如下:
# 当遍历第一个元素时，删除了下标为0的元素，
# 当遍历下标为1的元素时，后面的元素会向前移动一个位置，
# 就是元素2移动到了原来元素1的位置，
# 但是此时已经准备删除下标为1的元素，
# 这样就将元素2跳过去了，以此类推，
# 所有偶数元素都没有被删除。

# 最好的解决办法:对待删除列表进行浅拷贝并删除
list_demo_02 = copy.copy(list_demo)

for temp in list_demo_02:
    list_demo.remove(temp)

print list_demo


# 题目：输出 9*9 乘法口诀表
# for i in range(1, 10):
#     print
#     for j in range(1, i+1):
#         print "{}*{}={}".format(i, j, i*j),

# 一行打印九九乘法表x
print "\n".join([''.join(["\t{}*{}={}".format(x, y, y*x) for y in xrange(1, x+1)]) for x in xrange(1, 10)])
