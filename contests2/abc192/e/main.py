import heapq

N, M, X, Y = map(int, input().split())
X, Y = X - 1, Y - 1
graph = [[] for _ in range(N)]

for _ in range(M):
    A, B, T, K = map(int, input().split())
    A, B = A - 1, B - 1
    graph[A].append((B, T, K))
    graph[B].append((A, T, K))

mindist = [-1] * N
heap = []
heapq.heapify(heap)
heapq.heappush(heap, (0, X))
while heap:
    dist, node = heapq.heappop(heap)
    if mindist[node] != -1:
        continue
    mindist[node] = dist
    for i, t, k in graph[node]:
        if mindist[i] != -1:
            continue
        heapq.heappush(heap, (dist + t + (k - dist % k) % k, i))

print(mindist[Y])
