number = int(input())

def div(n):
    s_n = str(n)
    if('0' in s_n):
        return False
    for d in s_n:
        if(n % int(d) != 0):
            return False
    return True

if(number != 0):
    print("1", end="")

for n in range(2, number+1):
    if(div(n)):
        print("", n, end="")
