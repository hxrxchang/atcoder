N = int(input())
A = list(map(int, input().split()))

sum = [0] * N
for i, a in enumerate(A):
  if i == 0:
    sum[i] = a
  else:
    sum[i] = sum[i-1] + a

ans = float('inf')
for i in range(N):
  t = abs(sum[i] - (sum[-1] - sum[i]))
  ans = min(ans, t)

print(ans)
