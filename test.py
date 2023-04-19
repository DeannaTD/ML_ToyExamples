number = int(input())

for n in range(1, number + 1):
    s_n = str(n)
    div = True
    for d in s_n:
        if(d == '0'):
            div = False
            break
        if(n % int(d) != 0):
            div = False
            break
    if(div):
        print(n)
