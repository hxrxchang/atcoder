N, K = map(int, input().split())
H = [int(input()) for _ in range(N)]
H.sort()

ans = float('inf')
for i in range(N - K + 1):
  start = H[i]
  end = H[i + K - 1]
  ans = min(ans, end - start)

print(ans)
