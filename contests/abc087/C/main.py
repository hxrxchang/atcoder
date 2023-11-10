N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

ans = 0
for i in range(N):
  a1 = sum(A1[:i+1])
  a2 = sum(A2[i:])
  ans = max(ans, a1+a2)

print(ans)
