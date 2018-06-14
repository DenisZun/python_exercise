# encoding: utf-8


# 方法1
def yh_tri(n):
    L = []
    for _ in xrange(n):
        # 生成下一层数据（除第 1 位数之外），赋值给 L (第 2 步)
        L = [L[i] + L[i+1] for i in range(len(L)-1)]
        # 插入第 1 位数字 1，构成完整的下一层数据 (第 3 步)
        L.insert(0, 1)
        yield L
        # 末尾补位，为生成下一层数据做准备（第 1 步)
        L.append(0)

if __name__ == '__main__':
    for item in yh_tri(10):
        print item

# 方法2
def yh_tri_02(n):
    L, index = [1], 0
    while index < n:
        yield L
        L = [1] + [L[i] + L[i+1] for i in xrange(len(L) - 1)] + [1]
        index += 1

if __name__ == '__main__':
    for item in yh_tri_02(10):
        print item


# 方法3
def triangles(n):
    N, index = [1], 1
    while index < n:
        yield N
        N.append(0)
        N = [N[r - 1] + N[r] for r in range(len(N))]
        index += 1

if __name__ == '__main__':
    for i in triangles(11):
        print i