from collections import defaultdict

N = int(input())
cnt = defaultdict(int)

for _ in range(N):
  s = input()
  cnt[s] += 1

maxi = max(cnt.values())

words = []
for s in list(cnt.keys()):
  if cnt[s] == maxi:
    words.append(s)

words.sort()

for w in words:
  print(w)
