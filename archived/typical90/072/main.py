H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

max_length = -1

def dfs(start, now, count, visited):
    global max_length
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        nx, ny = now[0] + dx, now[1] + dy
        if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == '.':
            if start == (nx, ny) and count > 1:
                max_length = max(max_length, count + 1)
            elif not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(start, (nx, ny), count + 1, visited)
                # バックトラックで行き止まりから戻ってきたときに、再び訪れることができるようにする
                visited[nx][ny] = False

for i in range(H):
    for j in range(W):
        if grid[i][j] == '.':
            visited = [[False] * W for _ in range(H)]
            visited[i][j] = True
            start_i = i
            start_j = j
            dfs((i, j), (i, j), 0, visited)

print(max_length)
