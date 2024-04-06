S = input()
T = input()

for i in range(len(S)):
  if i == len(S) - 1 and S[i] == T[i]:
    print(len(T))
  elif i == len(S):
    print(len(S))
  if not S[i] == T[i]:
    print(i + 1)
    break

