import itertools

N, M = map(int, input().split())

S = []

for _ in range(N):
  S.append(input())

N = list(range(N))
cnt = 0

for c in itertools.combinations(N, 2):
  for i in range(M):
    if S[c[0]][i] == "x" and S[c[1]][i] == "x":
      break
    if i == M - 1:
      cnt += 1

print(cnt)
