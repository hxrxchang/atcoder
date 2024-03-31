N, A, B = map(int, input().split())
D = list(map(int, input().split()))

D2 = []
for d in D:
    D2.append(d % (A + B))
    D2.append((d % (A + B)) + A + B)

D = D2
D.sort()

# もとのD: [1, 2, 8]
# 円環に並べたD: [1, 2, 8, 11, 12, 18]
# としたとき、円環に並べたDの中で、長さがもとのDとなる連続部分列を取得し、その最後から最初を引いて、Aより小さかったらOK
half = len(D) // 2
for i in range(len(D) - half):
    diff = D[half - 1 + i] - D[i]
    if diff < A:
        print("Yes")
        exit()

print("No")
