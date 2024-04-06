N, A, B = map(int, input().split())
C = list(map(int, input().split()))

for i in range(N):
    c = C[i]
    if A + B == c:
        print(i + 1)
