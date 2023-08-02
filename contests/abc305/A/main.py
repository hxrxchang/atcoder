N = int(input())

ans = 0
for i in range(5, 101, 5):
  if abs(i - N) < abs(ans - N):
    ans = i

print(ans)
