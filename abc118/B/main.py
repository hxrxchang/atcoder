N, M = map(int, input().split())
foods = [0] * (M + 1)

for _ in range(N):
    A = list(map(int, input().split()))
    for i in range(1, A[0] + 1):
        foods[A[i]] += 1

print(foods.count(N))

