def climbing_leaderboard(scores, alice):
    res = []
    for i in alice:
        scores.append(i)
        scores.sort(reverse=True)
        ranking = dict()
        max = scores[0]
        position = 1
        for score in scores:
            if score == max:
                ranking[score] = position
            elif score < max:
                max = score
                position += 1
                ranking[score] = position

        res.append(ranking[i])
    return res


s = [100, 100, 40, 40, 50, 20, 10]
a = [5, 25, 50, 120]

s2 = [90, 90, 80, 75, 60, 100]
a2 = [50, 65, 77, 90, 102]

print(climbing_leaderboard(s, a))

