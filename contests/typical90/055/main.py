from itertools import combinations

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for comb in combinations(A, 5):
  if comb[0] % P * comb[1] % P * comb[2] % P * comb[3] % P * comb[4] % P== Q:
    cnt += 1

print(cnt)
