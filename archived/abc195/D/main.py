import copy

N, M, Q = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
# 価値の高い順、重さの軽い順にソート
items.sort(key=lambda x: (-x[1], x[0]))
boxes = list(map(int, input().split()))

for _ in range(Q):
  l, r = map(int, input().split())
  l, r = l - 1, r - 1
  boxes2 = boxes[:l] + boxes[r + 1:]
  boxes2.sort()
  items2 = copy.deepcopy(items)

  ans = 0
  # 容量の小さい箱から順に、入れられるアイテムの中で価値の高いものを入れる
  for capacity in boxes2:
    for item in items2:
      if item[0] <= capacity:
        ans += item[1]
        items2.remove(item)
        break

  print(ans)
