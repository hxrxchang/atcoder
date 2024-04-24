K = int(input())

visited = [False] * (K + 1)
tmp = 7 % K
cnt = 1

while True:
    rem = tmp % K
    if rem == 0:
        print(cnt)
        break
    if visited[rem]:
        print(-1)
        break
    visited[rem] = True
    tmp = tmp * 10 % K + 7 % K
    cnt += 1
