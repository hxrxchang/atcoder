N, T = map(int, input().split())
A = list(map(int, input().split()))

t = 0
i = 0
while t < T:
  t += A[i % N - 1]
  i += 1

if i % N == 0:
  ans = [N, A[N - 1] - (t - T)]
else:
  ans = [i % N, A[i % N] - (t - T)]
print(*ans)
