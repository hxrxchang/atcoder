H, W = map(int, input().split())
A = [list(input()) for i in range(H)]
B = [list(input()) for i in range(H)]

# (s, t) の組み合わせを全探索
for s in range(H):
    for t in range(W):
        jugde = True
        # A, B の各マスを全探索で比較
        for i in range(H):
            for j in range(W):
                if A[(i - s + H) % H][(j - t + W) % W] != B[i][j]:
                    jugde = False
        if jugde:
            print("Yes")
            exit()

print("No")
