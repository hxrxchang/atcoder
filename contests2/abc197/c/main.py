from functools import reduce
import operator

N = int(input())
A = list(map(int, input().split()))

if N == 1:
    print(A[0])
    exit()

ans = float('inf')

for i in range(2 ** (N - 1)):
    seperators = []
    for j in range(N - 1):
        if ((i >> j) & 1):
            seperators.append(j)
    if len(seperators) > 0:
        sections = []
        last = 0
        for s in seperators:
            sections.append(reduce(operator.or_, A[last:s + 1]))
            last = s + 1
        if last < N:
            sections.append(reduce(operator.or_, A[last:]))

        ans = min(ans, reduce(operator.xor, sections))
print(ans)
