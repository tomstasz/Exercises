def find_digits(n):
    digits = list(str(n))
    res = 0
    for i in digits:
        try:
            if n % int(i) == 0:
                res += 1
        except ZeroDivisionError:
            continue
    return res


print(find_digits(12))
print(find_digits(1012))
