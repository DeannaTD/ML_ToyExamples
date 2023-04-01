N = int(input())
f= []
for i in range(1, N+1):
    s = str(i)
    if(s.__contains__('0')):
        continue
    for j in s:
        if i % int(j) != 0:
            break
    else:
        f.append(i)
print(" ".join(map(str,f)))
