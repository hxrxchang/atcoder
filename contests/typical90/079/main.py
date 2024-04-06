H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

cnt = 0
for h in range(H - 1):
    for w in range(W - 1):
        if A[h][w] == B[h][w]:
            continue
        diff = B[h][w] - A[h][w]
        A[h][w] += diff
        A[h][w + 1] += diff
        A[h + 1][w] += diff
        A[h + 1][w + 1] += diff

        cnt += abs(diff)

if A == B:
    print("Yes")
    print(cnt)
else:
    print("No")
