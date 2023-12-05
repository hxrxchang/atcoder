N, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
# diff[i]: A[i]とA[i + 1]の差分
diffs = []
for i in range(N - 1):
  diff = A[i + 1] - A[i]
  diffs.append(diff)
  ans += abs(diff)

for _ in range(Q):
  L, R, V = map(int, input().split())
  L -= 1
  R -= 1
  if L > 0:
    prev_diff_L = diffs[L - 1]
    diffs[L - 1] += V
    ans += abs(diffs[L - 1]) - abs(prev_diff_L)
  if R < len(diffs):
    prev_diff_R = diffs[R]
    diffs[R] -= V
    ans += abs(diffs[R]) - abs(prev_diff_R)
  print(ans)
