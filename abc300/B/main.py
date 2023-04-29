H, W = map(int, input().split())
A = [list(input()) for i in range(H)]
B = [list(input()) for i in range(H)]

for i in range(H):
    a = A.pop(0)
    A.append(a)
    flag = True
    for j in range(H):
        a = A[j]
        b = B[j]
        if a.count("#") != b.count("#"):
            flag = False
            break
    if flag:
        break
    else:
        if i == H-1:
            print("No")
            exit()

A2 = [list(x) for x in zip(*A)]
B2 = [list(x) for x in zip(*B)]

for i in range(W):
    a = A2.pop(W - 1)
    A2.insert(0, a)
    flag = True
    for j in range(W):
        a = A2[j]
        b = B2[j]
        if a.count("#") != b.count("#"):
            flag = False
            break
    if flag:
        break
    else:
        if i ==  W-1:
            print("No")
            exit()

print("Yes")
