A, B, K = map(int, input().split())

numbers = set()

for i in range(K):
    if A + i > B:
        break
    numbers.add(A + i)
    numbers.add(B - i)

for i in sorted(list(numbers)):
    print(i)
