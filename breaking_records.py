
def breaking_records(arr):
    max = arr[0]
    min = arr[0]
    max_counter = 0
    min_counter = 0
    result = list()

    for i in arr:
        if i > max:
            max = i
            max_counter += 1
        if i < min:
            min = i
            min_counter += 1
    result.append(max_counter)
    result.append(min_counter)

    return result


arr = [10, 5, 20, 20, 4, 5, 2, 25, 1]

arr2 = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]


print(breaking_records(arr2))
