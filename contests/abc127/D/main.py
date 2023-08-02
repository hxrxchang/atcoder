from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

card_count= defaultdict(int)

for a in A:
  card_count[a] += 1

for _ in range(M):
  B, C = map(int, input().split())
  card_count[C] += B

card_nums = sorted(card_count.keys(), reverse=True)

ans = 0
cnt = 0
for c in card_nums:
  ans += c * card_count[c]
  cnt += card_count[c]
  if cnt >= N:
    break

if cnt > N:
  ans -= (cnt - N) * c

print(ans)

