from collections import deque

N = int(input())
P = list(map(int, input().split()))

que = deque()
dist = [-1] * (N + 1)
que.append(N)
dist[N] = 0

while(que):
  v = que.popleft()
  p = P[v - 2]
  if dist[p] == -1:
    que.append(p)
    dist[p] = dist[v] + 1

print(dist[1])
