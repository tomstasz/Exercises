import math


def chocolate_feast(n, c, m):
    res = 0
    chocolate_money = math.floor(n / c)
    chocolate_wrap = math.floor(chocolate_money / m)
    res += chocolate_money + chocolate_wrap
    rest = chocolate_wrap + chocolate_money % m
    while rest >= m:
        res += math.floor(rest / m)
        rest = math.floor(rest / m) + rest % m

    return res


print(chocolate_feast(10, 2, 5))  # 6
print(chocolate_feast(12, 4, 4))  # 3
print(chocolate_feast(6, 2, 2))  # 5
print(chocolate_feast(15, 3, 2))  # 9
print(chocolate_feast(43203, 60, 5))  # 899



