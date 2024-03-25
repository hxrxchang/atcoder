import heapq

def topological_sort(graph):
    in_degree = [0] * len(graph)
    for i in range(len(graph)):
        for j in graph[i]:
            in_degree[j] += 1

    heap = []
    heapq.heapify(heap)
    sorted_list = []

    for i in range(len(graph)):
        if in_degree[i] == 0:
            heapq.heappush(heap, i)

    while heap:
        u = heapq.heappop(heap)
        sorted_list.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heapq.heappush(heap, v)

    if len(sorted_list) == len(graph):
        return sorted_list
    else:
        return []

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append(b)

res = topological_sort(graph)
if len(res) == 0:
    print(-1)
else:
    ans = []
    for i in res:
        ans.append(i + 1)
    print(*ans)
