import itertools

numbers = []
for _ in range(3):
  for i in list(map(int, input().split())):
    numbers.append(i)

def is_gakkari(n):
  if numbers[n[0]] == numbers[n[1]] and numbers[n[2]] != numbers[n[1]]:
    return True
  if numbers[n[3]] == numbers[n[4]] and numbers[n[5]] != numbers[n[4]]:
    return True
  if numbers[n[6]] == numbers[n[7]] and numbers[n[8]] != numbers[n[7]]:
    return True
  if numbers[n[0]] == numbers[n[3]] and numbers[n[6]] != numbers[n[3]]:
    return True
  if numbers[n[1]] == numbers[n[4]] and numbers[n[7]] != numbers[n[4]]:
    return True
  if numbers[n[2]] == numbers[n[5]] and numbers[n[8]] != numbers[n[5]]:
    return True
  if numbers[n[0]] == numbers[n[4]] and numbers[n[8]] != numbers[n[4]]:
    return True
  if numbers[n[2]] == numbers[n[4]] and numbers[n[6]] != numbers[n[4]]:
    return True
  return False


perm = itertools.permutations(list(range(0, 9)), 9)

total = 0
gakkari_cnt = 0
for p in perm:
  total += 1
  if is_gakkari(p):
    gakkari_cnt += 1

ans = 1 - gakkari_cnt / total

print(ans)
