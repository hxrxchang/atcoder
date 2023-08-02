S = input()

if not len(S) == 8:
  print("No")
  exit()

if not S[0].isalpha():
  print("No")
  exit()

if not S[7].isalpha():
  print("No")
  exit()

try:
  if int(S[1:7]) < 100000:
    exit()
except:
  print("No")
  exit()

print("Yes")

