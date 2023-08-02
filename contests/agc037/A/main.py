S = list(input())
# dp[i]: i - 1文字まで見たときの最大の分割数
dp = [0] * (len(S))
dp[0] = 1

for i in range(1, len(S)):
  if S[i] == S[i - 1]:
    dp[i] = dp[i - 1]
  else:
    dp[i] = dp[i - 1] + 1

print(dp[-1])


