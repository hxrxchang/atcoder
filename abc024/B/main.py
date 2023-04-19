N, T = map(int, input().split())

cnt = 0
prev = int(input())
for _ in range(N - 1):
    curr = int(input())
    if curr - prev > T:
        cnt += T
    else:
        cnt += curr - prev
    prev = curr

cnt += T
print(cnt)
