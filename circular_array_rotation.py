def circular_array_rotation(a, k, q):
    res = list()
    for i in range(k):
        last = a.pop(-1)
        a.insert(0, last)
    for j in q:
        res.append(a[j])
    return res


a = [1, 2, 3]
k = 2
q = [0, 1, 2]

print(circular_array_rotation(a, k, q))