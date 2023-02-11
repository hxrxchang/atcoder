S = input()
S2 = ""
for s in S:
  if s == "0":
    S2 += "1"
  elif s == "1":
    S2 += "0"

print(S2)
