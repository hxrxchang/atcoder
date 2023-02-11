N, M = map(int, input().split())
G = []
for _ in range(M):
  input()
  A = list(map(int, input().split()))
  G.append(A)

cnt = 0
for i in range(2 ** M):
  ans = True
  temp = []
  for j in range(M):
    if (i >> j) & 1:
      temp += G[j]
  for i in range(1, N + 1):
    if not i in temp:
      ans = False
      break
  if ans:
    cnt += 1

print(cnt)
