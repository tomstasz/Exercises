def rot_left(a, d):
    for _ in range(0, d):
        num = a.pop(0)
        a.append(num)
    return a


a = [1, 2, 3, 4, 5]
d = 4

print(rot_left(a, d))