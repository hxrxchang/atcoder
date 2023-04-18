N = int(input())
N %= 30
A = ['1', '2', '3', '4', '5', '6']

for i in range(N):
    A[i % 5], A[i % 5 + 1] = A[i % 5 + 1], A[i % 5]

ans = ""
for a in A:
    ans += a

print(ans)
