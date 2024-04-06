H, W, N = map(int, input().split())
grid = [['.'] * W for _ in range(H)]

# 0: up, 1: right, 2: down, 3: left
dir = 0
h, w = 0, 0
for _ in range(N):
    if grid[h][w] == '.':
        grid[h][w] = '#'
        dir = (dir + 1) % 4
    else:
        grid[h][w] = '.'
        dir = (dir - 1) % 4
    if dir == 0:
        h -= 1
    elif dir == 1:
        w += 1
    elif dir == 2:
        h += 1
    elif dir == 3:
        w -= 1
    h %= H
    w %= W

for row in grid:
    print(''.join(row))
