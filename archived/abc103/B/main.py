S = input()
T = input()

for _ in range(len(T)):
  if S == T:
    print("Yes")
    exit()
  T = T[-1] + T[:-1]

print("No")
