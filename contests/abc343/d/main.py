from collections import defaultdict

N, T = map(int, input().split())

# 各人のスコアを記録する
scores = defaultdict(int)

# スコアの種類を記録する
set_scores = set()
set_scores.add(0)

# 誰がそのスコアを持っているかを記録する
scores2 = defaultdict(set)
for i in range(1, N + 1):
    scores2[0].add(i)

for i in range(T):
    a, b = map(int, input().split())
    current_score = scores[a]
    new_score = scores[a] + b
    scores2[current_score].remove(a)

    if len(scores2[current_score]) == 0:
        set_scores.remove(current_score)

    set_scores.add(new_score)
    scores2[new_score].add(a)
    scores[a] = new_score

    print(len(set_scores))
