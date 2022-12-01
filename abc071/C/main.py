N = int(input())
A = list(map(int, input().split()))
A.sort()

longest = 0
second_longest = 0

while True:
  if len(A) < 2:
    break
  a = A[-1]
  b = A[-2]
  if a == b:
    if longest == 0:
      longest = a
    else:
      second_longest = a
      break
    A.pop(-1)
    A.pop(-1)
  else:
    A.pop(-1)

print(longest * second_longest)
