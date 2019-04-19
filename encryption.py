from math import sqrt, ceil, floor


def encryption(s):
    s = ''.join(s.split(' '))
    enc_format = len(s)
    x = floor(sqrt(enc_format))
    y = ceil(sqrt(enc_format))
    while x * y < enc_format:
        x += 1

    rows = list()

    while s:
        row = s[:x+1]
        rows.append(row)
        s = s[x+1:]

    # res = """"""
    #
    # for i in rows:
    #     res += i
    #     res += '\n'
    res_u = list()

    # for word in rows:
    #     l = word[:1]
    #     res += l
    #     word = word[1:]
    for word in rows:
        res_u.append(list(word))

    res = list()
    final = list()
    while res_u:
        for i in res_u:
            if i:
                l = i.pop(0)
                res.append(l)
            else:
                res = ''.join(res)
                while res:
                    row = res[:x]
                    final.append(row)
                    res = res[x:]
                return final


print(encryption('have a nice day'))
print(encryption('if man was meant to stay on the ground god would have given us roots'))
print(encryption('chillout'))
print(encryption('feed the dog'))
