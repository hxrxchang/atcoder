from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
into_num = [0] * N

for _ in range(M):
  x, y = map(int, input().split())
  x -= 1
  y -= 1
  graph[y].append(x)
  into_num[x] += 1

que = deque()

# その時点での入次数が0の頂点の数
tmp = 0
for i in range(N):
  if into_num[i] == 0:
    tmp += 1
    que.append(i)

if tmp != 1:
  print("No")
  exit()

order = [0 for _ in range(N)]
# 未確定の頂点の数
rem = N

while True:
  current = que.popleft()
  tmp -= 1
  order[current] = rem
  rem -= 1

  if rem == 0:
    break

  for node in graph[current]:
    into_num[node] -= 1
    if into_num[node] == 0:
      que.append(node)
      tmp += 1

  if tmp != 1:
    print("No")
    exit()

print("Yes")
print(*order)
