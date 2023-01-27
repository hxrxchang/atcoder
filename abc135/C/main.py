N = int(input())
A = list(map(int, input().split()))
original_A = A.copy()
B = list(map(int, input().split()))

#B[i] は A[i] or A[i + 1] を倒せるので、後ろから倒していけばOK
for i in range(N - 1, -1, -1):
  val = B[i]
  a, b = A[i], A[i + 1]
  b_copy = b
  b -= val
  val -= b_copy
  if b < 0:
    a -= val
  if b < 0:
    b = 0
  if a < 0:
    a = 0
  A[i] = a
  A[i + 1] = b

cnt = 0
for i in range(N + 1):
  a = original_A[i]
  b = A[i]
  cnt += a - b

print(cnt)
