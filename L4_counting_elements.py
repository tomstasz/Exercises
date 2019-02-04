def solution(a):
    a.sort()
    smallest = 1
    for i in a:
        if i == smallest:
            smallest += 1

    return smallest


a_1 = [1, 3, 6, 4, 1, 2]
a_2 = [1, 2, 3]
a_3 = [-1, -3]


print(solution(a_1))
print(solution(a_2))
print(solution(a_3))