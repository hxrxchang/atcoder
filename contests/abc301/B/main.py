N = int(input())
A = list(map(int, input().split()))
A_ = [A[0]]

for i in range(N - 1):
    diff = A[i + 1] - A[i]
    if diff > 1:
        for j in range(1, diff):
            A_.append(A[i] + j)
    elif diff < -1:
        for j in range(-1, diff, -1):
            A_.append(A[i] + j)
    A_.append(A[i + 1])

print(*A_)
