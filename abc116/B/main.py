S = int(input())
A = [S]

def f(n):
  if n % 2 == 1:
    return 3 * n + 1
  else:
    return n / 2

current = 1
while True:
  a = f(A[current - 1])
  current += 1
  if a in A:
    break
  else:
    A.append(a)

print(current)


