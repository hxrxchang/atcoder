S = input()

new_S = ""
tmp = ""
for i in range(len(S)):
  s = S[i]
  if i % 2 == 1:
    tmp = s + tmp
    new_S += tmp
    tmp = ""
  else:
    tmp += s

print(new_S)
