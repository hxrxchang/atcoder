N, X = map(int, input().split())
coins = []

for _ in range(N):
    A, B = map(int, input().split())
    for i in range(B):
        coins.append(A)

dp = [False] * (X + 1)
dp[0] = True

for coin in coins:
    tmp = dp[:]
    for i in range(1, X + 1):
        if i - coin >= 0:
            tmp[i] = dp[i] or dp[i - coin]
    dp = tmp

if dp[X]:
    print("Yes")
else:
    print("No")

