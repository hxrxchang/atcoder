# 問題が意味不明。解いてて楽しくない。
N = int(input())
A = list(map(int, input().split()))

counter = {}
for a in A:
    counter[a] = counter.get(a, 0) + 1

unique_numbers = sorted(list(set(A)), reverse=True)

for n in unique_numbers:
    print(counter[n])
for i in range(N - len(unique_numbers)):
    print(0)
