N, K = map(int, input().split())
A = list(map(int, input().split()))

if K > A[-1]:
  print(-1)
else:
  left = 0
  right = N - 1
  while not left == right:
    mid = (left + right) // 2
    if A[mid] >= K:
      right = mid
    else:
      left = mid + 1
  print(left)

