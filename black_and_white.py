def black_and_white(b, w, bc, wc, z):
    black = b * bc
    white = w * wc
    black_convert = wc + z
    white_convert = bc + z

    if bc <= black_convert:
        black_cost = black
    else:
        black_cost = black_convert * b

    if wc <= white_convert:
        white_cost = white
    else:
        white_cost = white_convert * w

    return black_cost + white_cost


print(black_and_white(10, 10, 1, 1, 1))
print(black_and_white(5, 9, 2, 3, 4))
print(black_and_white(3, 6, 9, 1, 1))
print(black_and_white(7, 7, 4, 2, 1))
print(black_and_white(3, 3, 1, 9, 2))
