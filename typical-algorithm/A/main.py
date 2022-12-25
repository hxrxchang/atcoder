N, K = map(int, input().split())
A = list(map(int, input().split()))

ng = -1
ok = N

if A[-1] < K:
  print(-1)
else:
  while not ok - ng == 1:
    mid = (ok + ng) // 2
    if A[mid] >= K:
      ok = mid
    else:
      ng = mid
  print(ok)
