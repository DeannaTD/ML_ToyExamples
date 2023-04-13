s = input()
words = 0
n = False

for c in s:
    if(c != ' ' and n == False):
        words += 1
        n = True
    elif(c == ' ' and n == True):
        n = False

print(words)
