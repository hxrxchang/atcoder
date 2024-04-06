N, Q = map(int, input().split())
A = list(map(int, input().split()))

diff = 0
for _ in range(Q):
  T, X, Y = map(int, input().split())
  X, Y = X - 1, Y - 1
  if T == 1:
    X = (X - diff)
    Y = (Y - diff)
    A[X], A[Y] = A[Y], A[X]
  if T == 2:
    diff += 1
    diff %= N
  if T == 3:
    X = X - diff
    print(A[X])
