N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())

INF = 2 ** 60

for i in range(Q):
  B = int(input())
  left = 0
  right = N
  while right - left > 1:
    mid = (right + left) // 2
    if A[mid] <= B:
      left = mid
    else:
      right = mid

  ans = INF
  if right < N:
    ans = min(ans, abs(B - A[right]))
  if right > 0:
    ans = min(ans, abs(B - A[left]))
  print(ans)
