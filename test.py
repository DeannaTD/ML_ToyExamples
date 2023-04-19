number = int(input())

def div(n):
    s_n = str(n)
    for d in s_n:
        if(d == '0'):
            return False
        if(n % int(d) != 0):
            return False
    return True

for n in range(1, number):
    if(div(n)):
        print(n, end=" ")

if(div(number)):
    print(number)
