N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A + B
C.sort()


def binary_search(a, x):
  lo = 0
  hi = len(a) - 1
  while lo <= hi:
    mid = (lo + hi) // 2
    if a[mid] < x:
      lo = mid + 1
    elif a[mid] > x:
      hi = mid - 1
    else:
      return mid
  return -1

A_ = []
for a in A:
  A_.append(binary_search(C, a) + 1)

B_ = []
for b in B:
  B_.append(binary_search(C, b) + 1)


print(*A_)
print(*B_)
