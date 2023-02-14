N, A, B = map(int, input().split())
S = input()
temp_A, temp_B = 0, 0

for i in range(1, N + 1):
  s = S[i - 1]
  if s == "a":
    if temp_A + temp_B < A + B:
      print("Yes")
      temp_A += 1
    else:
      print("No")
  elif s == "b":
    if temp_A + temp_B < A + B and temp_B + 1 <= B:
      print("Yes")
      temp_B += 1
    else:
      print("No")
  else:
    print("No")
