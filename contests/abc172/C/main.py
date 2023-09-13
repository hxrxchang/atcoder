import bisect

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ruiseki_A = [0] * (N)
ruiseki_A[0] = A[0]
for i in range(1, N):
  ruiseki_A[i] = ruiseki_A[i - 1] + A[i]

ruiseki_B = [0] * (M)
ruiseki_B[0] = B[0]
for i in range(1, M):
  ruiseki_B[i] = ruiseki_B[i - 1] + B[i]

# 最初にAを1冊も読まない場合を計算
ans = bisect.bisect_right(ruiseki_B, K)
for ai in range(N):
  diff = K - ruiseki_A[ai]
  if diff < 0:
    break
  bi = bisect.bisect_right(ruiseki_B, diff)
  # aiは0indexedなので、0の時は1冊読んだことになるので+1する
  ans = max(ans, ai + 1 + bi)

print(ans)
