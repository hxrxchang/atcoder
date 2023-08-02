N, A, B = map(int, input().split())

cnt = 0
for i in range(1, N + 1):
    sum = 0
    for s in list(str(i)):
        sum += int(s)
    if A <= sum <= B:
        cnt += i

print(cnt)
