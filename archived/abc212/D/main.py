import heapq
heap = []
heapq.heapify(heap)

Q = int(input())
cnt = 0
for _ in range(Q):
  q = list(map(int, input().split()))
  if q[0] == 1:
    heapq.heappush(heap, q[1] - cnt)
  elif q[0] == 2:
    cnt += q[1]
  elif q[0] == 3:
    print(heapq.heappop(heap) + cnt)
