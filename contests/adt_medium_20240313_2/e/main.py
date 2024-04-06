from itertools import permutations
from sortedcontainers import SortedSet

S, K = input().split()
K = int(K)
S = list(S)

p_s = SortedSet()
for p in sorted(list(permutations(S))):
    p_s.add(''.join(p))

print(p_s[K-1])

