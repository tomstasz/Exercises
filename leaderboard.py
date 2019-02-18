def climbing_leaderboard(scores, alice):
    scores = list(set(scores))
    scores.sort(reverse=True)
    res = list()
    for a_score in alice:
        while scores and a_score >= scores[-1]:
            scores.pop()
        res.append(len(scores) + 1)
    return res


s = [100, 100, 40, 40, 50, 20, 10]
a = [5, 25, 50, 120]

s2 = [90, 90, 80, 75, 60, 100]
a2 = [50, 65, 77, 90, 102]

print(climbing_leaderboard(s, a))

