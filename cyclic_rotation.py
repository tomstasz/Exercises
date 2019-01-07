def solution(A, K):
    print(A[-K:] + A[:-K])


solution([3, 8, 9, 7, 6], 3)
solution([0, 0, 0], 1)
solution([1, 2, 3, 4], 4)
