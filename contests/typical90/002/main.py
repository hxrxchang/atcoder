N = int(input())

def check(st):
  if st.count("(") != st.count(")"):
    return False
  # stを先頭から一文字ずつチェックしていき、どのタイミングにおいても"("の数が")"を下回ることはない
  left_cnt = 0
  right_cnt = 0
  for s in st:
    if s == "(":
      left_cnt += 1
    elif s == ")":
      right_cnt += 1
    if left_cnt < right_cnt:
      return False
  return True

for i in range(2 ** N):
  st = ""
  for j in range(N - 1, -1, -1):
    if (i >> j) & 1:
      st += ")"
    else:
      st += "("
  if check(st):
    print(st)
