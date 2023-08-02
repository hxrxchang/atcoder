S = input()

for i, s in enumerate(S):
  if s == "A":
    start = i
    break

for i, s in enumerate(S[::-1]):
  if s == "Z":
    end = len(S) - i
    break

print(len(S[start:end]))
