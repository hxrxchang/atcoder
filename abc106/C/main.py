S = list(input())
K = int(input())

if S[0] != "1":
  print(S[0])
else:
  for i in range(K):
    if S[i] != "1":
      print(S[i])
      exit()
  print(1)

