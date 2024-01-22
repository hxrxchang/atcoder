H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

ans - -1
visited = [[False] * W for _ in range(H)]

