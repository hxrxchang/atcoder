import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0
for i in range(N):
  idx = bisect.bisect_right(A, A[i] + M)
  cnt = idx - i
  ans = max(ans, cnt)

print(ans)
