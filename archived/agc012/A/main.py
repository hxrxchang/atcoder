N = int(input())
# 強さの総和
cnt = 0
# 何チームできたか
cnt2 = 0

A = list(map(int, input().split()))
A.sort(reverse=True)

i = 1
while cnt2 < N:
  cnt += A[i]
  cnt2 += 1
  i += 2

print(cnt)
