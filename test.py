s = input()
words = []
word = ""
n = False

for c in s:
    if(c != ' ' and n == False):
        word += c
        n = True
    elif(c == ' ' and n == True):
        words.append(word)
        word = ""
        n = False
    elif(c != ' '):
        word += c

i = 0
for j in range(len(words)):
    if(len(words[i]) < len(words[j])):
        i = j
print(words[i])
print(len(words[i]))
