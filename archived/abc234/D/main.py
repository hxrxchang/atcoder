import heapq

N, K = list(map(int, input().split()))
P = list(map(int, input().split()))

heap = []
heapq.heapify(heap)

for i in range(K):
    heapq.heappush(heap, P[i])

item = heapq.heappop(heap)
print(item)

for i in range(K, N):
    if P[i] > item:
        heapq.heappush(heap, P[i])
        item = heapq.heappop(heap)
    print(item)

