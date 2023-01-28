N, M = map(int, input().split())
S = []
T = []
for _ in range(N):
  S.append(input())
for _ in range(M):
  T.append(input())

cnt = 0
for s in S:
  s = s[3:]
  for t in T:
    if s == t:
      cnt += 1
      break

print(cnt)
