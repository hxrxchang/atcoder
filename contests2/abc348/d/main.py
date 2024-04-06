from collections import defaultdict, deque

H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

start = (0, 0)
goal = (0, 0)

for i in range(H):
    for j in range(W):
        if grid[i][j] == "S":
            start = (i, j)
        if grid[i][j] == "T":
            goal = (i, j)


N = int(input())
medicines = defaultdict(int)
for _ in range(N):
    R, C, E = map(int, input().split())
    R, C = R-1, C-1
    medicines[(R, C)] = E


que = deque()
que.append(start)
energy = 0

dist = [[False] * W for _ in range(H)]

def dfs(path, position):
    x, y = position
    if not (0 <= x < len(grid) and 0 <= y < len(grid[0])) or grid[x][y] == '#' or position in path:
        return
    path.append(position)
    if position == goal:
        paths.append(path.copy())
        path.pop()
        return
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        dfs(path, (x + dx, y + dy))
    path.pop()

paths = []
dfs([], start)

for path in paths:
    node_len = len(path)
    energy = 0
    ok = True
    for i in range(node_len):
        x, y = path[i]
        if (x, y) in medicines:
            energy = max(energy, medicines[(x, y)])
        if energy == 0:
            ok = False
            break
    if ok:
        print("Yes")
        exit()

print("No")
