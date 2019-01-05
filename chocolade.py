s = [1, 2, 1, 3, 2]
d = 3
m = 2

s02 = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
d02 = 18
m02 = 7


def birthday(s, d, m):
    m_list = list()
    res = 0
    if len(s) <= m:
        for i in range(len(s)):
            for j in range(m):
                m_list.append(s[i + j])
        if sum(m_list) == d:
            res += 1
        m_list.clear()
    else:
        for i in range(len(s) - m + 1):
            for j in range(m):
                m_list.append(s[i + j])
                print('for ', j, ': ', m_list)
            if sum(m_list) == d:
                res += 1
            print('res: ', res)
            m_list.clear()

    print(res)


birthday(s, d, m)

birthday(s02, d02, m02)  # 3
