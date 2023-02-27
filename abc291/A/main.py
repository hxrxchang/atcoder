S = input()

for i in range(len(S)):
  s = S[i]
  if ord(s) < 97:
    print(i + 1)
    exit()
