N = int(input())
W = list(input().split())

for w in W:
  if w in ["and", "not", "that", "the", "you"]:
    print("Yes")
    exit()

print("No")
