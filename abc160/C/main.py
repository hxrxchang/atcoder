K, N = map(int, input().split())
A = list(map(int, input().split()))

longest = 0
for i in range(0, N - 1):
  if longest < A[i + 1] - A[i]:
    longest = A[i + 1] - A[i]

if longest < K - A[-1] + A[0]:
  longest = K - A[-1] + A[0]

ans = K - longest

print(ans)
