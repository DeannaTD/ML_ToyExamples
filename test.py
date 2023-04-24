s = input()

lengths = []
prev = s[0]
cl = 1
for i in range(1, len(s)):
    if(s[i] == prev):
        lengths.append(cl)
        cl = 0
    prev = s[i]
    cl += 1
else:
    lengths.append(cl)

print(max(lengths))
