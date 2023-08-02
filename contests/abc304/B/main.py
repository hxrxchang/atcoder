N = input()
if len(N) <= 3:
  print(N)
elif len(N) == 4:
  print(N[:3] + '0')
elif len(N) == 5:
  print(N[:3] + '00')
elif len(N) == 6:
  print(N[:3] + '000')
elif len(N) == 7:
  print(N[:3] + '0000')
elif len(N) == 8:
  print(N[:3] + '00000')
elif len(N) == 9:
  print(N[:3] + '000000')
