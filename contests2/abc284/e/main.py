import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * N
path = []
cnt = 0

def dfs(v):
    global cnt

    if cnt == 10 ** 6:
        return

    visited[v] = True
    cnt += 1

    for u in graph[v]:
        if not visited[u]:
            dfs(u)

    # バックトラック
    visited[v] = False
    # print(visited)

dfs(0)

print(cnt)
