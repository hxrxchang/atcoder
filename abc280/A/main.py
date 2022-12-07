H, W = map(int, input().split())
cnt = 0
for _ in range(H):
  c = input().count('#')
  cnt += c

print(cnt)
