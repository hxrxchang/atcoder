from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A2 = defaultdict(int)
B2 = defaultdict(int)
C2 = defaultdict(int)

for a in A:
  A2[a % 46] += 1

for b in B:
  B2[b % 46] += 1

for c in C:
  C2[c % 46] += 1

cnt = 0
for i in range(46):
  for j in range(46):
    for k in range(46):
      if (i + j + k) % 46 == 0:
        cnt += A2[i] * B2[j] * C2[k]

print(cnt)
