N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

X = int(input())

# dp[i]: i段目に登れるかどうか
dp = [False] * (X + 1)
dp[0] = True

# モチがあるかをO1で判定するためにメモ
memo_B = [False] * (X + 1)
for b in B:
  memo_B[b] = True

for i in range(1, X + 1):
  # モチがあるのであれば、その段には登れない
  if memo_B[i]:
    continue
  for a in A:
    if i >= a and dp[i - a]:
      dp[i] = True

if dp[X]:
  print("Yes")
else:
  print("No")
