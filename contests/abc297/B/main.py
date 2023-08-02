S = input()

B_idxes = []
R_idxes = []
K_idx = None
for i in range(len(S)):
  if S[i] == 'B':
    B_idxes.append(i)
  elif S[i] == 'R':
    R_idxes.append(i)
  elif S[i] == 'K':
    K_idx = i

def check_B(idxes):
  return idxes[0] % 2 != idxes[1] % 2

def check_K(R, K):
  return R[0] < K < R[1]

if check_B(B_idxes) and check_K(R_idxes, K_idx):
  print("Yes")
else:
  print("No")

