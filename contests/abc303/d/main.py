X, Y, Z = map(int, input().split())
T = input()

# T[:i]までを作って、dp[0]: CapsロックがOFF, dp[1]: CapsロックがON であるときの最小のコスト
dp = [float('inf')] * 2
dp[0] = 0
dp[1] = Z

for i in range(1, len(T) + 1):
    tmp = dp[:]
    target = T[i - 1]
    if target == 'a':
        dp[0] = min(tmp[0] + X, tmp[1] + Z + X, tmp[1] + Z + Y)
        dp[1] = min(tmp[0] + X + Z, tmp[0] + Z + Y, tmp[1] + Y)
    else:
        dp[0] = min(tmp[1] + X + Z, tmp[1] + Z + Y, tmp[0] + Y)
        dp[1] = min(tmp[1] + X, tmp[0] + Z + X, tmp[0] + Z + Y)

print(min(dp))
