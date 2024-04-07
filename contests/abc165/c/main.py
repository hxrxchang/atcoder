from itertools import combinations_with_replacement

N, M, Q = map(int, input().split())

conditions = [list(map(int, input().split())) for _ in range(Q)]

sequences = list(combinations_with_replacement(range(1, M + 1), N))

ans = 0
for s in sequences:
    score = 0
    for a, b, c, d in conditions:
        if s[b - 1] - s[a - 1] == c:
            score += d
    ans = max(ans, score)

print(ans)
