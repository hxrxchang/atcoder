A, B = map(int, input().split())

cnt = 0
if A == B:
  print(0)
  exit()

while A != B and (A != 0 and B != 0):
  if A > B:
    c = A // B
    d = A % B
    cnt += c
    A = d
  else:
    c = B // A
    d = B % A
    cnt += c
    B = d

print(cnt - 1)

