S = list(input())
T = list(input())

def match(x, y):
  if x == y or x == "?" or y == "?":
    return True
  return False

# S, Tの先頭からi文字がマッチするかどうか
pre = [False] * (len(T) + 1)
pre[0] = True #先頭からゼロ文字 = 何も選ばない なのでTrue
for i in range(len(T)):
  if not match(S[i], T[i]):
    break
  pre[i + 1] = True

# S, Tの末尾からi文字がマッチするかどうか
suf = [False] * (len(T) + 1)
suf[0] = True #末尾からゼロ文字 = 何も選ばない なのでTrue
S.reverse()
T.reverse()
for i in range(len(T)):
  if not match(S[i], T[i]):
    break
  suf[i + 1] = True

for i in range(len(T) + 1):
  # ex: len(T): 2 だとする
  # i = 0 のときは pre[0], suf[2]
  # i = 1 のときは pre[1], suf[1] になるようにしたい
  if pre[i] and suf[len(T) - i]:
    print("Yes")
  else:
    print("No")
