arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]


def migratory_birds(arr):
    bird_types = dict()
    counter = 0
    for i in range(max(arr) + 1):
        for number in arr:
            if number == i:
                counter += 1
        bird_types[i] = counter
        counter = 0
    print(bird_types)

    how_many = list()
    types = list()

    for v in bird_types.values():
        how_many.append(v)
    print(max(how_many))

    for k, v in bird_types.items():
        if v == max(how_many):
            types.append(k)
    print(min(types))


migratory_birds(arr)
