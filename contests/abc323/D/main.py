from heapq import heappush, heappop, heapify
from collections import defaultdict

N = int(input())
heap = []
heapify(heap)
slimes = defaultdict(int)
slimes_set = set()

for _ in range(N):
  s, c = map(int, input().split())
  slimes[s] = c
  heappush(heap, s)
  slimes_set.add(s)

while heap:
  s = heappop(heap)
  slimes_set.remove(s)
  c = slimes[s]
  if c < 2:
    continue
  else:
    monster_cnt = c // 2
    slimes[s * 2] += monster_cnt
    slimes[s] -= 2 * monster_cnt
    if s * 2 not in slimes_set:
      heappush(heap, s * 2)
      slimes_set.add(s * 2)

ans = sum(slimes.values())

print(ans)
