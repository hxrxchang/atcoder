A, B, C = list(map(int, input().split()))

if not (A % 2 == 0 and B % 2 == 0 and C % 2 == 0):
  print(0)
  exit()

original_A, original_B, original_C = A, B, C

cnt = 0
while True:
  cnt += 1
  a, b, c = A, B, C
  A = (b + c) / 2
  B = (a + c) / 2
  C = (a + b) / 2
  if not (A % 2 == 0 and B % 2 == 0 and C % 2 == 0):
    print(cnt)
    exit()
  if A == original_A and B == original_B and C == original_C:
    print(-1)
    exit()
