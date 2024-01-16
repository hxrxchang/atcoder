from collections import deque

a, n = map(int, input().split())

graph = [-1] * (n * 10)

que = deque()
graph[1] = 0
que.append(1)

while que:
  tmp = que.popleft()
  if tmp > 10 and tmp % 10 != 0:
    str_tmp = str(tmp)
    operated = int(str_tmp[-1] + str_tmp[:-1])
    if operated < len(graph) and graph[operated] == -1:
      graph[operated] = graph[tmp] + 1
      que.append(operated)

  if tmp * a < len(graph) and graph[tmp * a] == -1:
    graph[tmp * a] = graph[tmp] + 1
    que.append(tmp * a)

print(graph[n])
