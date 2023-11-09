N = int(input())
H = list(map(int, input().split()))

for i in range(N - 1, 1, -1):
  if H[i - 1] <= H[i]:
    continue
  elif H[i - 1] - H[i] == 1:
    H[i - 1] -= 1
  else:
    print('No')
    exit()

print('Yes')

