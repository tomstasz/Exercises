def kaprekar_numbers(p, q):
    kap_numbers = list()

    for number in range(p, q+1):
        number_as_str = str(number**2)
        d = len(str(number))
        l = number_as_str[:-d]
        r = number_as_str[-d:]
        r = int(r)
        if l:
            l = int(l)
        else:
            l = 0

        if l + r == number:
            kap_numbers.append(number)

    if kap_numbers:
        for i in kap_numbers:
            print(i, end=' ')
    else:
        print('INVALID RANGE')


kaprekar_numbers(1, 100)
kaprekar_numbers(10, 30)
