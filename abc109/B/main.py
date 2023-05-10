N = int(input())

first = input()
words = set()
words.add(first)
last_word = first

for _ in range(N - 1):
    word = input()
    if word in words or last_word[-1] != word[0]:
        print('No')
        exit()
    words.add(word)
    last_word = word

print('Yes')
