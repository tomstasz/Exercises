h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]


def designer_pdf_viewer(h, word):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    alfa_dict = dict(zip(abc, h))
    word_h = list()
    for letter in word:
        word_h.append(alfa_dict[letter])
    max_letter = max(word_h)

    return max_letter * len(word)


print(designer_pdf_viewer(h, 'abc'))
