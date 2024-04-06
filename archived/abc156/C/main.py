N = int(input())
X = list(map(int, input().split()))
X.sort()
ans = None
for a in range(X[0], X[-1] + 1):
  cnt = 0
  for b in X:
    cnt += (b - a) ** 2
  if ans == None or cnt <= ans:
    ans = cnt

print(ans)
