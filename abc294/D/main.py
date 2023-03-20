from heapq import heappop, heappush, heapify
from collections import deque

N, Q = map(int, input().split())

tmp = 0
que = []
heapify(que)
done = set()

for i in range(Q):
  E = list(map(int, input().split()))
  if E[0] == 1:
    tmp += 1
    heappush(que, tmp)
  elif E[0] == 2:
    done.add(E[1])
  else:
    while que[0] in done:
      heappop(que)
    print(que[0])

