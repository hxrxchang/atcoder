A, B = map(int, input().split())

ans = A + B

if A - B > ans:
  ans = A - B

if A * B > ans:
  ans = A * B

print(ans)
