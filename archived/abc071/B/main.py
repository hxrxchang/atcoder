import string

S = input()
memo = set()
for s in S:
    memo.add(s)

for s in string.ascii_lowercase:
    if s not in memo:
        print(s)
        exit()

print('None')
