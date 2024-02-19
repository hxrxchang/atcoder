import bisect

N = int(input())
A = list(map(int, input().split()))
sumA = sum(A)

if sumA % 10 != 0:
    print("No")
    exit()

A = A * 2
cum = [0] * len(A)

cum[0] = A[0]

for i in range(1, len(A)):
    cum[i] = cum[i-1] + A[i]

for i in range(N * 2):
    target = sumA // 10 + cum[i]
    found = bisect.bisect_left(cum, target)
    if 0 < found < N * 2 and cum[found] - cum[i] == sumA // 10:
        print("Yes")
        exit()

print("No")
