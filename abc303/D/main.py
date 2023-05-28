X, Y, Z = map(int, input().split())
S = input()

caps_on = False
if Y < Z:
  key = 'shift'
else:
  key = 'caps'

def time_a(next_str):
  global caps_on
  if caps_on == False:
    if next_str == 'a':
      if X < Z + Y:
        return X
      else:
        if caps_on:
          caps_on = False
        else:
          caps_on = True
        return Z + Y
    elif next_str == 'A':
      if X > Z + Y:
        if caps_on:
          caps_on = False
        else:
          caps_on = True
        return Z + Y
      else:
        return X
    elif next_str == '':
      if X < Z + Y:
        return X
      else:
        if caps_on:
          caps_on = False
        else:
          caps_on = True
        return Z + Y
  else:
    if next_str == 'a':
      if X < Z + Y:
        return X
      else:
        if caps_on:
          caps_on = False
        else:
          caps_on = True
        return Z + Y
    elif next_str == 'A':
      if X > Z + Y:
        if caps_on:
          caps_on = False
        else:
          caps_on = True
        return Z + Y
      else:
        return X
    elif next_str == '':
      if X < Z + Y:
        return X
      else:
        if caps_on:
          caps_on = False
        else:
          caps_on = True
        return Z + Y

def time_A(next_str):
  global caps_on
  if caps_on == True:
    if next_str == 'a':
      if X < Z + Y:
        return X
      else:
        if caps_on:
          caps_on = False
        else:
          caps_on = True
        return Z + Y
    elif next_str == 'A':
      if X > Z + Y:
        if caps_on:
          caps_on = False
        else:
          caps_on = True
        return Z + Y
      else:
        return X
    elif next_str == '':
      if X < Z + Y:
        return X
      else:
        if caps_on:
          caps_on = False
        else:
          caps_on = True
        return Z + Y
  else:
    if next_str == 'a':
      if X < Z + Y:
        return X
      else:
        if caps_on:
          caps_on = False
        else:
          caps_on = True
        return Z + Y
    elif next_str == 'A':
      if X > Z + Y:
        if caps_on:
          caps_on = False
        else:
          caps_on = True
        return Z + Y
      else:
        return X
    elif next_str == '':
      if X < Z + Y:
        return X
      else:
        if caps_on:
          caps_on = False
        else:
          caps_on = True
        return Z + Y

cnt = 0
for i in range(len(S)):
  s = S[i]
  if i == len(S) - 1:
    next_str = ''
  else:
    next_str = S[i+1]
  if s == 'a':
    cnt += time_a(next_str)
  elif s == 'A':
    cnt += time_A(next_str)

print(cnt)
