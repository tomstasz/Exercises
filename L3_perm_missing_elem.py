# def solution(array):
#     array.sort()
#     for i in range(1, len(array)):
#         if array[i] - array[i-1] != 1:
#             return array[i] - 1
#
#
# a = [2, 3, 1, 5]
#
#
# print(solution(a))


# def solution(array):
#     n = len(array) + 1
#     sum_n = (n * (n + 1)) / 2
#     return sum_n - sum(array)


# def solution(A):
#     length = len(A)
#     xor_sum = 0
#     for index in range(0, length):
#         xor_sum = xor_sum ^ (A[index] ^ (index + 1))
#     return xor_sum ^ (length + 1)


def solution(array):
    n = len(array) + 1  # +1 bo wydłużamy o brakujący element
    print('n: ', n)

    full = [i for i in range(1, n + 1)]  # znowu +1, żeby uchwycić końcówkę range
    print('full: ', full)

    return sum(full) - sum(array)


a = [2, 3, 1, 5]


print(solution(a))
