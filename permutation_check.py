def solution(A):
    A.sort()

    if len(A) == 1 and 1 in A:
        return 1
    elif len(A) >= 1 and 1 not in A:
        return 0
    else:
        for i in range(1, len(A)):
            if (A[i] - A[i - 1]) != 1:
                return 0

        return 1


print(solution([4, 1, 3, 2]))
print(solution([4, 1, 3]))
print(solution([3]))
