N = int(input())

ans = 1
for i in range(N):
  sum_per_dice = sum(list(map(int, input().split())))
  ans = (ans * sum_per_dice) % (10 ** 9 + 7)

print(ans)
