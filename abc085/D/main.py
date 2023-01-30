import math

N, H = map(int, input().split())
items = []
# Aが最大値となる刀を記録(Aが同値のものが複数ある場合、Bが最小になるものを選ぶ)
A, B = map(int, input().split())
max_a_item = {'A': A, 'B': B, 'idx': 0}
items.append(max_a_item)

for i in range(1, N):
  A, B = map(int, input().split())
  # Aが同値のものが複数ある場合、Bが最小になるものを選ぶ
  if (A == max_a_item['A'] and B < max_a_item['B']) or max_a_item['A'] < A:
    max_a_item = {'A': A, 'B': B, 'idx': i}
  items.append({'A': A, 'B': B})

items.pop(max_a_item['idx'])
items.sort(key=lambda x:x['B'], reverse=True)

# 投げる刀の中でBが最小値となるもののindex
min_b_idx = 0
for i in range(len(items)):
  if max_a_item['B'] < items[i]['B']:
    min_b_idx = i
  else:
    break

cnt = 0
if len(items):
  for i in range(min_b_idx + 1):
    H -= items[i]['B']
    cnt += 1
    if H < 0:
      print(cnt)
      exit()

if max_a_item['A'] >= max_a_item['B']:
  cnt += math.ceil(H / max_a_item['A'])
else:
  H -= max_a_item['B']
  cnt += 1
  cnt += math.ceil(H / max_a_item['A'])

print(cnt)
