S = input()

d = {
    'A': [],
    'B': [],
    'C': [],
}

for i, s in enumerate(S):
    d[s].append(i)

r = d['A'] + d['B'] + d['C']

if r == list(range(len(S))):
    print('Yes')
else:
    print('No')
