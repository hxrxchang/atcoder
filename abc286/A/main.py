import copy
N, P, Q, R, S = map(int, input().split())

A = list(map(int, input().split()))
B = copy.deepcopy(A)
A[P - 1:Q] = B[R - 1:S]
A[R - 1:S] = B[P - 1:Q]

print(*A)
