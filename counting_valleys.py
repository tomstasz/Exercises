def counting_valleys(n, s):
    sea_level = 0
    steps = list()
    number_of_valleys = 0

    for step in s:
        if step == "U":
            sea_level += 1
        elif step == "D":
            sea_level -= 1

        steps.append(sea_level)

    print(steps)
    for i in range(n):
        if steps[i] < 0 and steps[i + 1] == 0:
            number_of_valleys += 1
    print(number_of_valleys)


n = 8
s = 'UDDDUDUU'

counting_valleys(n, s)