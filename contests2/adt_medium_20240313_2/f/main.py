N, T = map(int, input().split())
A = list(map(int, input().split()))

T = T % sum(A)

time = 0
for i, a in enumerate(A):
    if time + a > T:
        print(i + 1, T - sum(A[:i]))
        break
    time += a
