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

mw = max(words, key=len)
print(mw)
print(len(mw))
