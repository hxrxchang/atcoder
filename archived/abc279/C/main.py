H, W = map(int, input().split())
S = []
T = []
for _ in range(H):
  S.append(input())

for _ in range(H):
  T.append(input())

ans = "Yes"
for i in range(H):
  s = S[i]
  t = T[i]
  sc = s.count("#")
  tc = t.count("#")
  if not sc == tc:
    ans = "No"
    break

print(ans)
