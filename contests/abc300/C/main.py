H, W = map(int, input().split())
g = [input() for _ in range(H)]

def ok(i, j):
    return 0 <= i < H and 0 <= j < W

def test(i, j, d):
    for x in [-d, +d]:
        for y in [-d, +d]:
            s, t = i + x, j + y
            if not ok(s, t) or g[s][t] != '#':
                return False
    return True

N = min(H, W)
ans = [0] * (N + 1)
for i in range(H):
    for j in range(W):
        if g[i][j] != '#':
            continue
        if test(i, j, 1):
            d = 1
            while test(i, j, d + 1):
                d += 1
            ans[d] += 1

print(*ans[1:])
