numbers = list(map(int, input().split()))
numbers.sort()
odd = []
even = []

for i in numbers:
  if i % 2 == 0:
    even.append(i)
  else:
    odd.append(i)

if len(odd) == 0 or len(even) == 0:
  A, B, C = numbers[0], numbers[1], numbers[2]
  print((C - A) // 2 + (C - B) // 2)
  exit()

numbers = []
if len(even) > len(odd):
  for i in even:
    numbers.append(i + 1)
  numbers.append(odd[0])
else:
  for i in odd:
    numbers.append(i + 1)
  numbers.append(even[0])

numbers.sort()
A, B, C = numbers[0], numbers[1], numbers[2]

cnt = 1

while A < C - 1:
  A += 2
  cnt += 1

while B < C - 1:
  B += 2
  cnt += 1

if not A == C and not B == C:
  cnt += 1

print(cnt)
