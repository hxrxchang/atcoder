import copy

H_A, W_A = map(int, input().split())
A = [list(input()) for _ in range(H_A)]

H_B, W_B = map(int, input().split())
B = [list(input()) for _ in range(H_B)]

H_X, W_X = map(int, input().split())
X = [list(input()) for _ in range(H_X)]

sample = [['.'] * 10 for _ in range(10)]

def check(target, i, j):
  for h in range(H_X):
    for w in range(W_X):
      if target[h + i][w + j] != X[h][w]:
        return False
  return True

for i in range(10):
  if i + H_A > 9:
    continue
  for j in range(10):
    if j + W_A > 9:
      continue
    target = copy.deepcopy(sample)
    for h in range(H_A):
      for w in range(W_A):
        if target[i + h][j + w] == '.' and A[h][w] == '.':
          target[i + h][j + w] = '.'
        else:
          target[i + h][j + w] = '#'
    for k in range(10):
      if k + H_B > 9:
        continue
      for l in range(10):
        if l + W_B > 9:
          continue
        for h2 in range(H_B):
          for w2 in range(W_B):
            if target[k + h2][l + w2] == '.' and B[h2][w2] == '.':
              target[k + h2][l + w2] = '.'
            else:
              target[k + h2][l + w2] = '#'
            if check(target, i, j):
              print("Yes")
              exit()

print("No")
