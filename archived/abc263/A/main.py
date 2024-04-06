from collections import defaultdict

A = list(map(int, input().split()))

d = defaultdict(int)

for a in A:
  d[a] += 1

card_keys = list(d.keys())

if len(card_keys) != 2:
  print("No")
else:
  if d[card_keys[0]] == 2 or d[card_keys[1]] == 2:
    print("Yes")
  else:
    print("No")
