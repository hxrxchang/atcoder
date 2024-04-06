N, S, T = map(int, input().split())
tmp = 0
cnt = 0
for _ in range(N):
    A = int(input())
    tmp += A
    if S <= tmp <= T:
        cnt += 1

print(cnt)
