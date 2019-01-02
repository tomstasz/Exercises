

def count_apples_and_oranges(s, t, a, b, apples, oranges):
    apple_res = 0
    orange_res = 0

    for apple in apples:
        if s <= a + apple <= t:
            apple_res += 1

    for orange in oranges:
        if s <= b + orange <= t:
            orange_res += 1

    print('apples:', apple_res)
    print('oranges:', orange_res)


count_apples_and_oranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])
count_apples_and_oranges(7, 10, 4, 12, [2, 3, -4], [3, -2, -4])
count_apples_and_oranges(2, 3, 1, 5, [2], [-2])
