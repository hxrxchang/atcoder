def update(n):
  while n > 100:
    n = n // 100
  return n

print(update(10 ** 8))
