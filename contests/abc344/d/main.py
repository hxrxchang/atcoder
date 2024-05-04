T = input()
N = int(input())

bags = []
for _ in range(N):
    inp = input().split()
    inp[0] = int(inp[0])
    bags.append(inp)

# dp[i]: Tのi文字目までをいくらで作れるか(最小金額)
dp = [float('inf')] * (len(T) + 1)
dp[0] = 0

for i in range(N):
    tmp = dp[:]
    for item in bags[i][1:]:
        for j, d in enumerate(dp):
            if d == float('inf'):
                continue
            if item == T[j:j + len(item)]:
                dp[j + len(item)] = min(tmp[j + len(item)], tmp[j] + 1)

print(dp[-1] if dp[-1] != float('inf') else -1)
