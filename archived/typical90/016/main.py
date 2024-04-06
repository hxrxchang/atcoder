N = int(input())
coins = list(map(int, input().split()))

ans = 10000
for x in range(0, 10000):
  for y in range(0, 10000):
    diff = N - (coins[0] * x + coins[1] * y)
    if diff >= 0 and diff % coins[2] == 0:
      tmp = x + y + diff // coins[2]
      if tmp < ans:
        ans = tmp

print(ans)
