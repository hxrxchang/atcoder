H, N = map(int, input().split())
magics = []
for _ in range(N):
  A, B = map(int, input().split())
  C = A / B
  magics.append((A, B, C))

magics.sort(key=lambda x: (-x[2], x[1]))

cnt = 0

for i, m in enumerate(magics):
  if H <= m[0]:
    cnt += m[1]
    break
  else:
    d = H // m[0]
    cnt += d * m[1]
    H = H % m[0]
    if H == 0:
      break

print(cnt)
