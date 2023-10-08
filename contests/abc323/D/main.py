from heapq import heappush, heappop, heapify
from collections import defaultdict

N = int(input())
heap = []
heapify(heap)
slimes = defaultdict(int)

for _ in range(N):
  s, c = map(int, input().split())
  slimes[s] = c
  heappush(heap, s)

while heap:
  s = heappop(heap)
  c = slimes[s]
  if c >= 2:
    monster_cnt = c // 2
    slimes[s * 2] += monster_cnt
    heappush(heap, s * 2)
    slimes[s] -= 2 * monster_cnt

ans = sum(slimes.values())
print(ans)
