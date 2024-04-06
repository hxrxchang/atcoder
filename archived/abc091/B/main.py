from collections import defaultdict

cards = set()
blue_cards = defaultdict(int)
red_cards = defaultdict(int)

N = int(input())
for _ in range(N):
  s = input()
  cards.add(s)
  blue_cards[s] += 1

M = int(input())
for _ in range(M):
  t = input()
  cards.add(t)
  red_cards[t] += 1

ans = 0
for card in cards:
  if red_cards[card] > blue_cards[card]:
    continue
  ans = max(ans, blue_cards[card] - red_cards[card])

print(ans)
