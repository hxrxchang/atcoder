N = int(input())
A = list(map(int, input().split()))

colors = set()
cnt_stop = 0

for a in A:
  if a <= 399:
    colors.add('灰')
  elif 400 <= a <= 799:
    colors.add('茶')
  elif 800 <= a <= 1199:
    colors.add('緑')
  elif 1200 <= a <= 1599:
    colors.add('水')
  elif 1600 <= a <= 1999:
    colors.add('青')
  elif 2000 <= a <= 2399:
    colors.add('黄')
  elif 2400 <= a <= 2799:
    colors.add('橙')
  elif 2800 <= a <= 3199:
    colors.add('赤')
  elif 3200 <= a:
    cnt_stop += 1

min_cnt = len(colors) if len(colors) > 0 else 1
max_cnt = len(colors) + cnt_stop
print(min_cnt, max_cnt)
