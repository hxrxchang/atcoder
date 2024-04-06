A, B = map(int, input().split())

for i in range(0, 10):
  if i != A + B:
    print(i)
    break
