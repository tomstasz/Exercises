def sock_merchant(n, ar):
    no_duplicates = set(ar)
    print('no_d: ', no_duplicates)
    counter = 0
    pairs = list()

    for i in no_duplicates:
        for j in ar:
            if i == j:
                counter += 1
        pairs.append(int(counter / 2))
        counter = 0
    return sum(pairs)


n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]


print(sock_merchant(n, ar))
