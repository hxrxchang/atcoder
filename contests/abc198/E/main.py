import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
C = list(map(int, input().split()))

graph = [[] for _ in range(N)]
for _ in range(N - 1):
  A, B = map(int, input().split())
  A -= 1
  B -= 1
  graph[A].append(B)
  graph[B].append(A)

visited = [False] * (N + 1)
color = [False] * (10 ** 5 + 1)
