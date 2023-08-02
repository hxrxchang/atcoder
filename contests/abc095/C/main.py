A, B, C, X, Y = map(int, input().split())

ans = float('inf')
for i in range(2 * 10 ** 5 + 1):
  amount_c = i * C
  remain_a = max(0, X - i // 2)
  remain_b = max(0, Y - i // 2)
  amount_a = remain_a * A
  amount_b = remain_b * B
  ans = min(ans, amount_a + amount_b + amount_c)

print(ans)
