import heapq

N = int(input())
A = [int(input()) for _ in range(N)]
heap = []
heapq.heapify(heap)
for a in A:
    heapq.heappush(heap, -a)

for a in A:
    b = heapq.heappop(heap)
    b = -b
    if a == b:
        c = heapq.heappop(heap)
        c = -c
        print(c)
        heapq.heappush(heap, -c)
    else:
        print(b)
    heapq.heappush(heap, -b)
