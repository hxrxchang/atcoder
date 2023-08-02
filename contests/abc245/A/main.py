A, B, C, D = map(int, input().split())

if A > C:
  print('Aoki')
elif C > A:
  print("Takahashi")
elif B > D:
  print("Aoki")
else:
  print("Takahashi")
