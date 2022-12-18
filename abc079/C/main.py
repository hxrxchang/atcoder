S = input()
A, B, C, D = [int(s) for s in S]
op_cnt = len(S) - 1
for i in range(2 ** op_cnt):
  op = ["-"] * op_cnt
  for j in range(op_cnt):
    if ((i >> j) & 1):
      op[op_cnt - 1 - j] = "+"

  formula = ""
  for a, b in zip(S, op + [""]):
    formula += (a + b)
  if eval(formula) == 7:
    print(formula + "=7")
    break

