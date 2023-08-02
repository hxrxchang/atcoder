X = int(input())

def isprime(N):
  if N < 2:
    return False
  i = 2
  while i * i <= N:
    if N % i == 0:
      return False
    i += 1
  return True

while not isprime(X):
  X += 1

print(X)

