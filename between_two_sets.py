a = [2, 4]
b = [16, 32, 96]

c = [1]
d = [100]


def getTotalX(a, b):
    b_factors = list()
    res = list()
    for i in range(1, max(b) + 1):
        if all(b_factor % i == 0 for b_factor in b):
            b_factors.append(i)

    for b_factor in b_factors:
        if all(b_factor % a_number == 0 for a_number in a):
            res.append(b_factor)

    print(b_factors)
    print(res)


getTotalX(a, b)

getTotalX(c, d)