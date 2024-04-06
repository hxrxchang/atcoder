S = input()

for i in range(1, len(S)):
  if i % 2 == 1:
    if S[i] != "0":
      print("No")
      exit()

print("Yes")
