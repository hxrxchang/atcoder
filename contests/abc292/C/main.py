N = int(input())

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

memo = [0] * N
patterns = []
left, right = 1, N - 1
while left <= right:
  patterns.append([left, right])
  left += 1
  right -= 1

cnt = 0
for p in patterns:
  left, right = p[0], p[1]
  if memo[left] == 0:
    memo[left] = len(make_divisors(left))
  if memo[right] == 0:
    memo[right] = len(make_divisors(right))
  if left == right:
    cnt += memo[left] * memo[right]
  else:
    cnt += memo[left] * memo[right] * 2

print(cnt)

# print(memo)
# print(patterns)
