from heapq import heappush, heappop

N, M = map(int, input().split())
AtoB = [[] for _ in range(M + 1)]

for _ in range(N):
  A, B = map(int, input().split())
  if A > M:
    continue
  AtoB[A].append(B)

ans = 0

que = []

for B in AtoB:
  for b in B:
    heappush(que, -b)
  if que:
    ans += abs(heappop(que))

print(ans)
