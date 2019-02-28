def beautiful_days(i, j, k):
    reverse = [num - int(str(num)[::-1]) for num in range(i, j + 1)]
    b_days = 0
    for day in reverse:
        if day % k == 0:
            b_days += 1
    print(str(b_days))


beautiful_days(20, 23, 6)
