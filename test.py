number = int(input())

def div(n):
    s_n = set(str(n))
    for d in s_n:
        if(d == "0"):
            return False
        if(n % int(d) != 0):
            return False
    return True

if(number != 0):
    print("1", end="")

for n in range(2, number+1):
    if(div(n)):
        print("", n, end="")
