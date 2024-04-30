import math

N = int(input())
T = list(map(int, input().split()))

sum_T = sum(T)
dp = [False] * (sum_T + 1)
dp[0] = True

for t in T:
    tmp = dp[:]
    for time in range(1, sum_T + 1):
        if time - t >= 0:
            tmp[time] = dp[time] or dp[time - t]
    dp = tmp

for i in range(math.ceil(sum_T / 2), sum_T + 1):
    if dp[i]:
        print(i)
        break
