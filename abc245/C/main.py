N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def calc(a, b):
  return abs(a - b) <= K

dp_A = [False] * N
dp_B = [False] * N
dp_A[0] = True
dp_B[0] = True

for i in range(N - 1):
  if dp_A[i]:
    if calc(A[i], A[i + 1]):
      dp_A[i + 1] = True
    if calc(A[i], B[i + 1]):
      dp_B[i + 1] = True
  if dp_B[i]:
    if calc(B[i], A[i + 1]):
      dp_A[i + 1] = True
    if calc(B[i], B[i + 1]):
      dp_B[i + 1] = True


if dp_A[-1] or dp_B[-1]:
  print("Yes")
else:
  print("No")
