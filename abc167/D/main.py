import math

N, K = map(int, input().split())
A = list(map(int, input().split()))
A = [a - 1 for a in A]  # 0-indexedに変更

logK = int(math.log2(K)) + 1
doubling = [[0] * N for _ in range(logK)]

for i in range(N):
  doubling[0][i] = A[i]

for k in range(logK - 1):
  for i in range(N):
    doubling[k + 1][i] = doubling[k][doubling[k][i]]

now = 0
for k in range(logK):
  if K & 1:
    now = doubling[k][now]
  K = K >> 1

print(now + 1)

