N, Q = map(int, input().split())
cards = []
for _ in range(N):
  cards.append(0)

for _ in range(Q):
  E = input().split(" ")
  query_type, player = int(E[0]), int(E[1])
  player -= 1
  if query_type == 1:
    cards[player] = cards[player] + 1
  elif query_type == 2:
    cards[player] = cards[player] + 2
  else:
    if cards[player] < 2:
      print("No")
    else:
      print("Yes")
