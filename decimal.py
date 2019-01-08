arr = [-4, 3, -9, 0, 4, 1]


def plus_minus(array):
    positive = []
    negative = []
    zero = []

    for i in array:
        if i > 0:
            positive.append(i)
        elif i < 0:
            negative.append(i)
        else:
            zero.append(i)

    print(positive)
    print(negative)
    print(zero)
    pos = format(len(positive) / len(array), '.6f')
    neg = format(len(negative) / len(array), '.6f')
    ze = format(len(zero) / len(array), '.6f')

    print(pos)
    print(neg)
    print(ze)


plus_minus(arr)
