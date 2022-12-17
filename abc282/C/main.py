N = int(input())
S = input()

first = S.find('"')
last = S.rfind('"')

s1 = S[0:first]
s3 = S[last + 1:len(S)]
s2 = S[first:last]

s1 = s1.replace(",", ".")
s3 = s3.replace(",", ".")
print(s1 + s2 + s3)
