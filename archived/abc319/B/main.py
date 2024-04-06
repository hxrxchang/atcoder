N = int(input())

yakusu = []
for i in range(1, 10):
  if N % i == 0:
    yakusu.append(i)

ans = ""
for i in range(N + 1):
  if i == 0:
    ans += str(yakusu[0])
  else:
    found = False
    for j in yakusu:
      if N % j == 0 and i % (N / j) == 0:
        ans += str(j)
        found = True
        break
    if not found:
      ans += "-"

print(ans)
