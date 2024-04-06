N = int(input())
H = list(map(int, input().split()))

cnt = 0
tmp_cnt = 0
for i in range(1, N):
    if H[i] <= H[i - 1]:
        tmp_cnt += 1
    else:
        cnt = max(cnt, tmp_cnt)
        tmp_cnt = 0

cnt = max(cnt, tmp_cnt)
print(cnt)

