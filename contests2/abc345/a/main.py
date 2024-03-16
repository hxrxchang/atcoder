S = list(input())

if S[0] == "<" and S[-1] == ">" and "<" not in S[1:len(S) - 2] and ">" not in S[1:len(S) - 1]:
    print("Yes")
else:
    print("No")

