N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = "Yes"
diff = 0
for i in range(N):
  a = A[i]
  b = B[i]
  diff += abs(a - b)

if diff > K:
  print("No")
  exit()
if diff % 2 != K % 2:
  print("No")
  exit()

print("Yes")

