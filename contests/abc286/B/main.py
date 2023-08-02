N = int(input())
S = list(input())

prev = ""
ans = ""
for s in S:
  if prev + s == "na":
    ans += "ya"
  else:
    ans += s
  prev = s

print(ans)
