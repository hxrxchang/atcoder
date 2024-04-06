N = int(input())
T, A = map(int, input().split())
T = T * 1000
A = A * 1000

H = list(map(int, input().split()))

candidate = 0
candidate_data = T - H[0] * 6

for i in range(1, len(H)):
    tmp = T - H[i] * 6
    if abs(A - candidate_data) > abs(A - tmp):
        candidate = i
        candidate_data = tmp

print(candidate + 1)
