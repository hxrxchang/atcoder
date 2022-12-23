import sys
sys.setrecursionlimit(10 ** 6)

H, W = map(int, input().split())
graph = []
visited = []
s = None
g = None
for i in range(H):
  row = input()
  if "s" in row:
    j = row.index("s")
    s = [i, j]
  if "g" in row:
    j = row.index("g")
    g = [i, j]
  graph.append(row)
  visited_row = [False] * W
  visited.append(visited_row)


def dfs(x, y):
  if x < 0 or y < 0 or x >= H or y >= W:
    return
  if graph[x][y] == "g":
    print("Yes")
    exit()
  if graph[x][y] == "#":
    return
  if visited[x][y] == True:
    return
  else:
    visited[x][y] = True
  dfs(x - 1, y)
  dfs(x + 1, y)
  dfs(x, y + 1)
  dfs(x, y - 1)

dfs(s[0], s[1])
print("No")
