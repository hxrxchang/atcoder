from numpy import base_repr

N, K = map(int, input().split())

for _ in range(K):
  dec = int(str(N), 8)
  nine_dec = base_repr(dec, 9)
  tmp = ""
  for s in str(nine_dec):
    if s == "8":
      tmp += "5"
    else:
      tmp += s
  N = int(tmp)

print(N)
