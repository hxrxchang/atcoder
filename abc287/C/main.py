from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for i in range(M):
  A, B = map(int, input().split())
  A -= 1
  B -= 1
  if len(graph[B]):
    b = graph[B][0]

  graph[A].append(B)
  graph[B].append(A)

