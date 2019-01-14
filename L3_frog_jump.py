import math

# Method 1

# def solution(x, y, d):
#     counter = 0
#     while x < y:
#         x += d
#         counter += 1
#     return counter


# Method 2

def solution(x, y, d):
    dist = y - x
    res = dist / d
    return math.ceil(res)


x = 10
y = 85
d = 30

print(solution(x, y, d))
