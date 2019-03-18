def library_fine(d1, m1, y1, d2, m2, y2):
    if y1 <= y2 and m1 <= m2 and d1 <= d2:
        return 0

    if y1 > y2:
        return (y1 - y2) * 10000
    elif y1 < y2:
        return 0

    if m1 > m2:
        return (m1 - m2) * 500
    elif m1 < m2:
        return 0

    if d1 > d2:
        return (d1 - d2) * 15


print(library_fine(9, 6, 2015, 6, 6, 2015))
print(library_fine(2, 7, 1014, 1, 1, 1015))
print(library_fine(28, 2, 2015, 15, 4, 2015))
print(library_fine(1, 1, 2015, 31, 12, 2014))
