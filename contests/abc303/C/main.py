from collections import defaultdict

N, M, H, K = map(int, input().split())
S = input()
points = defaultdict(int)
for _ in range(M):
  x, y = map(int, input().split())
  points[str(x) + ":" + str(y)] += 1

cnt = H
x, y = 0, 0
for i in range(N):
  cnt -= 1
  if S[i] == 'R':
    x = x + 1
    y = y
  elif S[i] == 'L':
    x = x - 1
    y = y
  elif S[i] == "U":
    x = x
    y = y + 1
  elif S[i] == "D":
    x = x
    y = y - 1
  if cnt < 0:
    print("No")
    exit()
  if points[str(x) + ":" + str(y)] > 0:
    if cnt < K:
      cnt = K
      points[str(x) + ":" + str(y)] -= 1

print("Yes")

