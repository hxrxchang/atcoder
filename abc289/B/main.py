N, M = map(int, input().split())
numbers = []
for i in range(1, N + 1):
  numbers.append(i)
# N = 2
if M == 0:
  print(*numbers)
  exit()

A = list(map(int, input().split()))
# A = [1]

ans = []
temp = [numbers[0]]
for i in range(N - 1):
  if numbers[i] in A:
    temp.insert(0, numbers[i + 1])
  else:
    ans += temp
    temp = [numbers[i + 1]]
ans += temp

print(*ans)
