N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())

# dp[i]段目に False: 登れない、True: 登れる
dp = [False] * (X + 1)
# 0段目には登れる
dp[0] = True

# M大きいので探索不要になるように全indexの結果を保存しておく
available = [True] * (X + 1)
for b in B:
  available[b] = False

for i in range(1, X + 1):
  if not available[i]:
    continue
  for a in A:
    # iのa段前がTrueなら、iにたどり着ける
    if i >= a and dp[i - a]:
      dp[i] = True

print("Yes" if dp[X] else "No")
