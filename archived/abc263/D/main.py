N, L, R = map(int, input().split())
A = list(map(int, input().split()))
reversed_A = A[::-1]

# dp_L[i]: 左から最小になるように選んでいく方法で、左からi個確認した際の累積和
dp_L = [0] * (N + 1)
# dp_R[i]: 右から最小になるように選んでいく方法で、右からi個確認した際の累積和
dp_R = [0] * (N + 1)

for i in range(1, N + 1):
  dp_L[i] = min(dp_L[i - 1] + A[i - 1], L * i)
  dp_R[i] = min(dp_R[i - 1] + reversed_A[i - 1], R * i)

ans = float('inf')
for i in range(N + 1):
  j = N - i
  ans = min(ans, dp_L[i] + dp_R[j])

print(ans)
