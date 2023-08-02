N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

def check(A, B):
    idxs = []
    for i in range(N):
        for j in range(N):
            if A[i][j]:
                idxs.append([i, j])
    for idx in idxs:
        for i, j in idxs:
            if not B[i][j]:
                return False
    return True


cnt = 0
while cnt < 4:
    if check(A, B):
        print("Yes")
        exit()
    A2= []
    for i in range(N):
        A2_ = []
        for j in range(N):
            A2_.append(A[N - 1 - j][i])
        A2.append(A2_)
    A = A2
    cnt += 1

print("No")

