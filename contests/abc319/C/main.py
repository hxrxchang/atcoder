import itertools

numbers = []
for _ in range(3):
  for i in list(map(int, input().split())):
    numbers.append(i)

comb = itertools.combinations(list(range(0, 9)), 2)

cnt = 0
gakkari_cnt = 0
for c in comb:
  for n in [item for item in list(range(0, 9)) if item not in list(c)]:
    cnt += 1
    if numbers[c[0]] == numbers[c[1]] and numbers[c[1]] != numbers[n]:
      gakkari_cnt += 1

print(gakkari_cnt)
ans = 1 - (gakkari_cnt / len(list(itertools.combinations(list(range(0, 9)), 3))))
print(ans)
