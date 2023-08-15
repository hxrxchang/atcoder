N, C = map(int, input().split())
events = [list(map(int, input().split())) for _ in range(N)]

days = set()
for event in events:
  days.add(event[0])
  days.add(event[1] + 1)

days = sorted(list(days))

zaatsu = {day: i for i, day in enumerate(days)}

imosu = [0] * (len(days))
for A, B, C2 in events:
  imosu[zaatsu[A]] += C2
  imosu[zaatsu[B + 1]] -= C2

for i in range(len(days) - 1):
  imosu[i + 1] += imosu[i]

ans = 0
for i in range(len(days) - 1):
  ans += min(C, imosu[i]) * (days[i + 1] - days[i])

print(ans)
