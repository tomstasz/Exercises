def get_money_spent(keyboards, drives, b):  # electronics shop
    result = list()
    for k in keyboards:
        for d in drives:
            if k + d <= b:
                result.append(k + d)

    if result:
        return max(result)
    else:
        return -1


k = [40, 50, 60]
d = [5, 8, 12]
b = 60


print(get_money_spent(k, d, b))
