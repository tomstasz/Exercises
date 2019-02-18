def climbing_leaderboard(scores, alice):
    scores = list(set(scores))
    scores.sort(reverse=True)
    ranking = [scores[0]]
    for score in scores[1:]:
        if score < ranking[-1]:
            ranking.append(score)
    res = list()
    for a_score in alice:
        while ranking and a_score >= ranking[-1]:
            ranking.pop()
        res.append(len(ranking) + 1)
    return res


s = [100, 100, 40, 40, 50, 20, 10]
a = [5, 25, 50, 120]

s2 = [90, 90, 80, 75, 60, 100]
a2 = [50, 65, 77, 90, 102]

print(climbing_leaderboard(s, a))

