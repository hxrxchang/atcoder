from collections import Counter

S = input()

if len(S) <= 2:
  if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
    print("Yes")
  else:
    print("No")
  exit()

cnt = Counter(S)

for i in range(104, 1000, 8):
  char = str(i)
  if not Counter(char) - cnt:
    print("Yes")
    exit()

print("No")
