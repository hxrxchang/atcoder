N, H = map(int, input().split())
items = []

# Aが最大値となる刀を記録
A, B = map(int, input().split())
max_a_item = {'A': A, 'B': B, 'idx': 0}
items.append({'A': A, 'B': B})

for i in range(1, N):
  A, B = map(int, input().split())
  # Aが同値の場合、Bが大きい方を残したいからBが小さい方にする
  if (A == max_a_item['A'] and B < max_a_item['B']) or max_a_item['A'] < A:
    max_a_item = {'A': A, 'B': B, 'idx': i}
  items.append({'A': A, 'B': B})

items.pop(max_a_item['idx'])
items.sort(key=lambda x:x['B'], reverse=True)

cnt = 0
for item in items:
  H -= item['B']
  cnt += 1
  if H < 0:
    print(cnt)
    exit

print(H, max_a_item['A'])
if H % max_a_item['A'] != 0:
  cnt += H // max_a_item['A'] + 1
else:
  cnt += H // max_a_item['A']

print(cnt)
