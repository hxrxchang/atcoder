import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)

N = int(input())

nodes = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

dist = [-1] * (N + 1)
dist[1] = 0

d_even = [1]
d_odd = []

que = deque()
que.append(1)

while que:
    current = que.popleft()
    next_nodes = nodes[current]
    for node in next_nodes:
        if dist[node] == -1:
            dist[node] = dist[current] + 1
            que.append(node)
            if dist[node] % 2 == 0:
                d_even.append(node)
            else:
                d_odd.append(node)

if len(d_even) >= len(d_odd):
    print(*d_even[:N // 2])
else:
    print(*d_odd[:N // 2])
