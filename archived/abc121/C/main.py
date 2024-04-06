N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

A.sort(key=lambda x: x[0])

cnt_amount = 0
cnt_count = 0

for a in A:
  money_per_count = a[0]
  purchase_max = a[1]
  if cnt_count + purchase_max <= M:
    cnt_amount += money_per_count * purchase_max
    cnt_count += purchase_max
    if cnt_count == M:
      break
  else:
    cnt_amount += money_per_count * (M - cnt_count)
    cnt_count += M - cnt_count
    break

print(cnt_amount)
