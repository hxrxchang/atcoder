S = input()
st = ""
st_list = []
for s in S:
  if s in ["A", "C", "G", "T"]:
    st += s
  else:
    st_list.append(len(st))
    st = ""
st_list.append(len(st))

print((max(st_list)))
