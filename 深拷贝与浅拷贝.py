import copy

a = [1,2,3,4,5]
b = ["A","B",a]

c = copy.copy(b)
print c

a[0] = 10
print c

c = copy.deepcopy(b)
print c

a[0] = 100
print a
print c

