#The Fastest way to cast a spell.
n , m = list(map(int,input().split()))
all_words = []
for i in range(m):
    words = list(input().split())
    all_words.append(words)
given_line = list(input().split())
for i in range(len(given_line)):
    for j in range(len(all_words)):
        if given_line[i] == all_words[j][0]:
            if len(given_line[i])>len(all_words[j][1]):
                given_line[i] = all_words[j][1]

print(" ".join(map(str,given_line)))