
from collections import defaultdict, deque

N = int(input())
graph = defaultdict(list)

for _ in range(N):
  A, B = map(int, input().split())
  graph[A].append(B)
  graph[B].append(A)

que = deque()
que.append(1)
S = {1}

while que:
  v = que.popleft()
  for i in graph[v]:
    if not i in S:
      que.append(i)
      S.add(i)

print(max(S))
