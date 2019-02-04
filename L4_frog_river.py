# def solution(x, a):
#     distance = [i for i in range(1, x + 1)]
#     indexes = list()
#     for i in distance:
#         if i in a:
#             indexes.append(a.index(i))
#         else:
#             return -1
#     return max(indexes)


def solution(X, A):
    covered = 0
    covered_a = [-1] * X
    for index, element in enumerate(A):
        if covered_a[element - 1] == -1:
            covered_a[element - 1] = element
            covered += 1
            if covered == X:
                return index
    return -1


a = [1, 3, 1, 4, 2, 3, 5, 4]


print(solution(5, a))