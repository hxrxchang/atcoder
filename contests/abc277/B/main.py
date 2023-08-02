
N = int(input())
checked = []
for _ in range(N):
  s = input()
  if s in checked:
    print("No")
    exit()
  else:
    checked.append(s)
  if not s[0] in ["H", "D", "C", "S"]:
    print("No")
    exit()
  if not s[1] in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
    print("No")
    exit()

print("Yes")

