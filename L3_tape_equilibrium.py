# def solution(a):
#     res = list()
#     for p in range(1, len(a)):
#         split_1 = a[:p]
#         split_2 = a[p:]
#         res.append(abs(sum(split_1) - sum(split_2)))
#         print('s_1: ', split_1)
#         print('s_2: ', split_2)
#     return min(res)


def solution(A):
    split_1 = A[0]
    split_2 = sum(A[1:])
    min_dif = abs(split_1 - split_2)
    for index in range(1, len(A) - 1):
        split_1 += A[index]
        split_2 -= A[index]
        if abs(split_1 - split_2) < min_dif:
            min_dif = abs(split_1 - split_2)
    return min_dif


arr = [3, 1, 2, 4, 3]

print(solution(arr))