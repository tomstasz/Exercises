def utopian_tree(n):
    grow = 1
    for i in range(1, n+1):
        if i % 2 != 0:
            grow *= 2
        elif i % 2 == 0:
            grow += 1

    return grow


print(utopian_tree(5))



