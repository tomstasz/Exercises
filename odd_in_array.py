# Rozwiązanie 1
#
# import collections
#
#
# def solution(array):
#     unique = [x for x, y in collections.Counter(array).items() if y == 1]
#     print(unique)
#
#
# Rozwiązanie 2
#
#
# def solution(array):
#     flag = True
#
#     while flag:
#         el = array.pop(0)
#         if el in array:
#             array.append(el)
#         else:
#             flag = False
#             print(el)


from collections import Counter


def solution(A):
    cnt = Counter()
    for i in A:
        cnt[i] += 1
    for x, y in cnt.items():
        if y == 1:
            print(x)


solution([9, 3, 9, 3, 9, 7, 9])
solution([-2, 8, 10, 8, 10])

