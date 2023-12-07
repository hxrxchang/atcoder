from sortedcontainers import SortedList
from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

S = SortedList(list(range(max(A) + 2)))
ans = []
tmp = defaultdict(int)
for i in range(M):
  tmp[A[i]] += 1
  if A[i] in S:
    S.remove(A[i])

ans.append(S.pop(0))

for i in range(M, N):
  tmp[A[i]] += 1
  if A[i] in S:
    S.remove(A[i])

  tmp[A[i-M]] -= 1
  if tmp[A[i-M]] == 0:
    S.add(A[i-M])

  if len(S) > 0:
    ans.append(S.pop(0))

print(min(ans))
