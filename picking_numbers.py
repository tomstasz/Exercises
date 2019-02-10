def picking_numbers(a):
    a.sort()
    res = list()
    counter = 0
    actual = a[0]

    if len(set(a)) == 1:
        res.append(len(a))

    for i in range(1, len(a)):

        if a[i] - actual <= 1:
            counter += 1
            res.append(counter)
        else:
            counter += 1
            res.append(counter)
            counter = 0
            actual = a[i]

    return max(res)


arr = [4, 6, 5, 3, 3, 1]
arr2 = [1, 2, 2, 3, 1, 2]
arr3 = [66 for i in range(100)]
print(len(arr3))
print(picking_numbers(arr3))