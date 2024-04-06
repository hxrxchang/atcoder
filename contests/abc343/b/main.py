N = int(input())

for i in range(N):
    A = list(map(int, input().split()))
    ans = []
    for i, a in enumerate(A):
        if a == 1:
            ans.append(i+1)
    print(*ans)
