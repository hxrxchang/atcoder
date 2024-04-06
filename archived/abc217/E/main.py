import heapq

N = int(input())

A = []
heap = []
heapq.heapify(heap)

for _ in range(N):
  Q = list(map(int, input().split()))
  if Q[0] == 1:
    A.append(Q[1])
  elif Q[0] == 2:
    if len(heap) > 0:
      print(heapq.heappop(heap))
    else:
      print(A.pop(0))
  else:
    for a in A:
      heapq.heappush(heap, a)
    A = []

