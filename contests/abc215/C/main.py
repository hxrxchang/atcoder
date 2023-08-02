from itertools import permutations

S, K = input().split()
S, K = list(S), int(K)
S.sort()
P = list(permutations(S))
P2_set = set()
P2 = []
for p in P:
  if not p in P2_set:
    P2_set.add(p)
    P2.append(p)

print(''.join(P2[K - 1]))
