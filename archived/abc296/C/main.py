N, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

for a in A:
  target = X + a
  left, right = 0, N - 1
  while left <= right:
    mid = (left + right) // 2
    if A[mid] == target:
      print("Yes")
      exit()
    elif A[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

print("No")

