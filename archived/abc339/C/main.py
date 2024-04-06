N = int(input())
A = list(map(int, input().split()))

cnt = 0
for a in A:
    cnt += a
    if cnt < 0:
        cnt = 0

print(cnt)
