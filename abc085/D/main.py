import math

N, H = map(int, input().split())
max_a = 0
B = []
for i in range(N):
  a, b = map(int, input().split())
  if max_a < a:
    max_a = a
  B.append(b)

throw_items = []
for i in range(len(B)):
  if max_a < B[i]:
    throw_items.append(B[i])
throw_items.sort(reverse=True)

cnt = 0
for item in throw_items:
  H -= item
  cnt += 1
  if H <= 0:
    print(cnt)
    exit()

cnt += math.ceil(H / max_a)

print(cnt)
