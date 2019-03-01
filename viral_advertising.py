import math


def viral_advertising(n):
    shared = 5
    total = 0
    days = dict()
    for day in range(1, n + 1):
        liked = math.floor(shared / 2)
        total += liked
        shared = liked * 3
        days[day] = total

    return days[n]


print(viral_advertising(5))
