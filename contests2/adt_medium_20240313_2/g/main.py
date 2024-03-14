from collections import deque

H , W = map(int, input().split())
graph = [list(input()) for _ in range(H)]

que = deque()
visited = [[False] * W for _ in range(H)]

snuke = {
    's': 'n',
    'n': 'u',
    'u': 'k',
    'k': 'e',
    'e': 's'
}

if graph[0][0] == 's':
    que.append(((0, 0), 's'))
    visited[0][0] = True

while que:
    cur = que.popleft()
    pos, s = cur[0], cur[1]
    h, w = pos[0], pos[1]
    next_s = snuke[s]
    for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        next_h, next_w = h + dh, w + dw
        if 0 <= next_h < H and 0 <= next_w < W and not visited[next_h][next_w] and graph[next_h][next_w] == next_s:
            que.append(((next_h, next_w), next_s))
            visited[next_h][next_w] = True

if visited[H - 1][W - 1]:
    print('Yes')
else:
    print('No')
