A = list(map(int, input().split()))

ans = 0
for i, a in enumerate(A):
  ans += a * 2 ** i

print(ans)
