W, N = map(int, input().split())

# 座標圧縮
blocks = []
points = []
for _ in range(N):
    L, R = map(int, input().split())
    points.append(L)
    points.append(R)
    blocks.append((L, R))
points = sorted(list(set(points)))
point_idx = {x: i + 1  for i, x in enumerate(points)}

H = [0] * (len(points) + 1)

for b in blocks:
    L, R = b[0], b[1]
    L = point_idx[L]
    R = point_idx[R]
    maximum = max(H[L:R + 1])
    for i in range(L, R + 1):
        H[i] = maximum + 1
    print(maximum + 1)

