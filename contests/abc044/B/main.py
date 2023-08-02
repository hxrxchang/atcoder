from collections import defaultdict

W = input()
memo = defaultdict(int)

for w in W:
    memo[w] += 1

for m in memo.keys():
    if memo[m] % 2 != 0:
        print("No")
        exit()

print("Yes")
