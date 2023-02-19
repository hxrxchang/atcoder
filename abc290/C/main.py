from collections import Counter
N, K = map(int, input().split())
A = list(map(int, input().split()))
A = Counter(A)

for i in range(K):
  if A[i] == 0:
    i -= 1
    break

print(i + 1)

