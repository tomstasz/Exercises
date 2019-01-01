
def solution(N):
    binary = format(N, 'b')
    res = []
    for i in binary:
        res.append(str(i))

    print(res)

    counter = 0
    zeros = []
    for num in range(len(res)):
        if res[num] == '0':
            counter += 1
        elif res[num] == '1':
            zeros.append(counter)
            counter = 0

    print(max(zeros))


solution(529)
solution(9)
solution(20)
solution(32)
solution(15)

