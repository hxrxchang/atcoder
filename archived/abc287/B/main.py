N, M = map(int, input().split())
S = []

for _ in range(N):
  S.append(input())

T = []
for _ in range(M):
  T.append(input())

cnt = 0
for s in S:
  if s[3:] in T:
    cnt += 1

print(cnt)
