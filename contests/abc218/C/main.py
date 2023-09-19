N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]

def find_left_top(S):
  for i in range(N):
    for j in range(N):
      if S[i][j] == '#':
        return i, j

def check(S,T):
	Si,Sj = find_left_top(S)
	Ti,Tj = find_left_top(T)
	offset_i = Ti-Si
	offset_j = Tj-Sj
	for i in range(N):
		for j in range(N):
			ii = i+offset_i
			jj = j+offset_j
			if 0<=ii<N and 0<=jj<N:
				if S[i][j]!=T[ii][jj]: return False
			else:
				if S[i][j]=='#': return False
	return True

def check_(S, T):
  s_left_top = find_left_top(S)
  t_left_top = find_left_top(T)
  offset_i, offset_j = t_left_top[0] - s_left_top[0], t_left_top[1] - s_left_top[1]
  for i in range(N):
    for j in range( N):
      i2, j2 = i + offset_i, j + offset_j
      if 0 <= i2 < N and 0 <= j2 < N and S[i][j] != T[i2][j2]:
        return False
      else:
        if S[i][j] == '#':
          return False
  return True

def rotate(S):
  S2 = []
  for i in range(N):
    s2 = []
    for j in range(N):
      s2.append(S[N -1 -j][i])
    S2.append(s2)
  return S2

cnt_s, cnt_t = 0, 0
for i in range(N):
  for j in range(N):
    if S[i][j] == '#':
      cnt_s += 1
    if T[i][j] == '#':
      cnt_t += 1
if cnt_s != cnt_t:
  print('No')
  exit()

for _ in range(3):
  if check(S, T):
    print('Yes')
    exit()
  S = rotate(S)

print('No')
