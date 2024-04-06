N = input()

if len(N) == 1:
  print("Yes")
  exit()

temp = int(N[0])
for i in range(1, len(N)):
  current = int(N[i])
  if temp <= current:
    print("No")
    exit()
  temp = current

print("Yes")
