N = int(input())

word = []
for i in range(N):
    word.append(input())

word = list(set(word))
word.sort(key=lambda x: (len(x), x))

for i in word:
    print(i)
