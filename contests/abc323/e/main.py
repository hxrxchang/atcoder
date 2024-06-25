MOD = 998244353
n, x = map(int, input().split())
t = list(map(int, input().split()))

invN = pow(n, MOD - 2, MOD)

dp = [0] * (x + 1)
dp[0] = 1
for i in range(1, x + 1):
    for j in range(n):
        if i - t[j] >= 0:
            dp[i] += (dp[i - t[j]] * invN) % MOD
            dp[i] %= MOD

print(dp)
result = 0
for i in range(x + 1):
    if i + t[0] > x:
        result += (dp[i] * invN) % MOD
        result %= MOD

print(result)
