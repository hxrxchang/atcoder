H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
B = [list(input()) for _ in range(H)]

for s in range(H):
    for t in range(W):
        flag = True
        for i in range(H):
            for j in range(W):
                if A[(s + i) % H][(t + j) % W] != B[i][j]:
                    flag = False
                    break
                if not flag:
                    break
        if flag:
            print("Yes")
            exit()

print("No")
