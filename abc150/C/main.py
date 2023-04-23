import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

permutations = list(itertools.permutations(range(1, N + 1)))

for i in range(len(permutations)):
    if list(permutations[i]) == P:
        p = i
    if list(permutations[i]) == Q:
        q = i

print(abs(p - q))
