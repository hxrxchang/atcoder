N = int(input())
prev = []
for _ in range(N):
  S = input()
  if S[0] in ['H','D', 'S', 'C'] and S[1] in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'] and S not in prev:
    prev.append(S)
    continue
  else:
    print("No")
    exit()

print("Yes")
