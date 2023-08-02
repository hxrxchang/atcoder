N = int(input())
for_cnt = 0
for _ in range(N):
  if input() == "For":
    for_cnt += 1

if for_cnt > N / 2:
  print("Yes")
else:
  print("No")
