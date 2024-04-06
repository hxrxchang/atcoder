N, M = map(int, input().split())

# 整数を与えると、約数がリストで返ってくる
def make_divisors(n):
  lower_divisors , upper_divisors = [], []
  i = 1
  while i*i <= n:
    if n % i == 0:
      lower_divisors.append(i)
      if i != n // i:
        upper_divisors.append(n//i)
    i += 1
  return lower_divisors + upper_divisors[::-1]

while True:
  diviros = make_divisors(M)
  if len(diviros) == 1:
    print(M)
    exit()
  for i in range(1, len(diviros)):

  if diviros[1] > N:
    print(-1)
    exit()
  M += 1
