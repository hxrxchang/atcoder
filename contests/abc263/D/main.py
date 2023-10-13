N, L, R = map(int, input().split())
A = list(map(int, input().split()))

sum_A = sum(A)
dp = [sum_A] * N

left = 0
right = N - 1

if L < A[left]:
  dp[0] = dp[0] - A[left] + L
  left += 1

if R < A[right]:
  dp[0] = dp[0] - A[right] + R
  right -= 1

