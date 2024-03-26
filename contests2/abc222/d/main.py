N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 998244353

# dp[i]: A, Bのi番目までの見たときにC[i]になりえる最小値、最大値、個数
dp = [{'max': 0, 'min': 0, 'count': 0} for _ in range(N)]
dp[0]['max'] = B[0]
dp[0]['min'] = A[0]
dp[0]['count'] = (B[0] - A[0] + 1) % MOD

for i in range(1, N):
    dp[i]['max'] = B[i]
    dp[i]['min'] = A[i]
    dp[i]['count'] = dp[i - 1]['count'] * (dp[i]['max'] - dp[i]['min'] + 1) % MOD

print(dp[N - 1]['count'])

