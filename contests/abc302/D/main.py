N, M, D = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

i = N - 1
j = M - 1

while (i >= 0 and j >= 0):
  if abs(A[i] - B[j]) <= D:
    print(A[i] + B[j])
    exit()
  else:
    if A[i] > B[j]:
      i -= 1
    else:
      j -= 1

print(-1)
