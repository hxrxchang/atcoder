N = int(input())
A = list(map(int, input().split()))

current = A[0]
tmp_cnt = 1
cnt = N
right = 1
left = 0

while right < N:
  if current < A[right]:
    current = A[right]
    tmp_cnt += 1
    right += 1
  else:
    cnt += (tmp_cnt * (tmp_cnt - 1)) // 2
    tmp_cnt = 1
    left = right
    current = A[right]
    right += 1

cnt += (tmp_cnt * (tmp_cnt - 1)) // 2

print(cnt)
