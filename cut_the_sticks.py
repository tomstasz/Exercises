def cut_the_sticks(arr):
    elements = list()
    while arr:
        elements.append(len(arr))
        minimum = min(arr)
        while minimum in arr:
            arr.remove(minimum)
        sub = [i - minimum for i in arr]
        print(sub)

    return elements


print(cut_the_sticks([5, 4, 4, 2, 2, 8]))
print(cut_the_sticks([1, 2, 3, 4, 3, 3, 2, 1]))
