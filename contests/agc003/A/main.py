S = input()

if 'N' in S and 'S' not in S:
  print("No")
  exit()
if 'S' in S and 'N' not in S:
  print("No")
  exit()
if 'W' in S and 'E' not in S:
  print("No")
  exit()
if 'E' in S and 'W' not in S:
  print("No")
  exit()

print("Yes")
