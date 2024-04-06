import bisect

N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sorted_A = sorted(A)
sorted_B = sorted(B)

ruiseki_b = [sorted_B[0]]
for i in range(1, M):
  ruiseki_b.append(ruiseki_b[i - 1] + sorted_B[i])

ans = 0
for i in range(N):
  a = sorted_A[i]
  target = bisect.bisect_right(sorted_B, P - a)
  ans += (i + 1) * a * ruiseki_b[target - 1]
  if target != M:
    ans += P * (M - target)

print(ans)


