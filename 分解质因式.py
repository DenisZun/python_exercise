# encoding: utf-8

def prime_num(num):
    r_value = []
    for i in range(2, num+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            r_value.append(i)
    return r_value  # 返回质数列表


def prime_factory_slove(num, prime_list):
    for n in prime_list:
        if num % n == 0:
            return [n, num/n]  # 开始分解


def prime_divisor(num):
    """外圈函数控制指引式分解的循环"""
    prime_list = prime_num(num)
    ret_vale = []

    while num not in prime_list:
        factor_list = prime_factory_slove(num, prime_list)
        print factor_list
        ret_vale.append(factor_list[0])
        num = factor_list[1]
    else:
        ret_vale.append(num)

    return ret_vale

if __name__ == '__main__':
    print prime_divisor(120)