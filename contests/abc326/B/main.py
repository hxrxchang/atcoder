N = int(input())

def jugde(N):
  N = str(N)
  N = list(N)
  if int(N[0]) * int(N[1]) == int(N[2]):
    return True
  return False

while N < 1000:
  if jugde(N):
    print(N)
    exit()
  N += 1
