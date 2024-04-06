N = int(input())
A = list(map(int, input().split()))

a = A[0]

for i in range(1, N):
  if a != A[i]:
    print('No')
    exit()

print('Yes')
