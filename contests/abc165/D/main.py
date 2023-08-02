A, B, N = map(int, input().split())

def solve(x):
  return A * x // B - A * (x // B)

## ↓で周期性を確認, Bの回数で周期性がある
# for i in range(100):
#   print(i, solve(i))

ans = 0
ans = max(ans, solve(N))
if B - 1 <= N:
  ans = max(ans, solve(B - 1))

print(ans)
