def kang(x1, v1, x2, v2):

    if (x1 > x2 and v1 > v2 or x1 < x2 and v1 < v2) or v1-v2 == 0:
        print('no')
        return "NO"
    if((x1 - x2) % (v2 - v1)) == 0:
        print('yes')
        return "YES"
    else:
        print('no')
        return "NO"


kang(0, 3, 4, 2)
kang(0, 2, 5, 3)
