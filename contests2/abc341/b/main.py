N = int(input())
A = list(map(int, input().split()))

for i in range(N - 1):
  S, T = map(int, input().split())
  if A[i] >= S:
    c = A[i] // S
    A[i] %= S
    A[i + 1] += T * c

print(A[-1])
