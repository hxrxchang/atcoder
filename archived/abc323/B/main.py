N = int(input())
S = [list(input()) for _ in range(N)]

ranking = [[i] for i in range(N)]

for i, s in enumerate(S):
  cnt = 0
  for s_ in s:
    if s_ == "o":
      cnt += 1
  ranking[i].append(cnt)

ranking.sort(key=lambda x: x[1], reverse=True)

ans = []
for r in ranking:
  ans.append(r[0])

print(*ans)

