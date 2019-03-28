def equalize_array(arr):
    length = len(arr)
    counter_list = list()
    counter = 0
    for i in sorted(arr):
        while i in arr:
            arr.remove(i)
            counter += 1
        counter_list.append(counter)
        counter = 0
    max_repeated = max(counter_list)
    result = length - max_repeated
    return result


print(equalize_array([3, 3, 2, 1, 3]))
print(equalize_array([1, 2, 2, 3]))
