def is_comprime(a,b):
    if(a<b):
        a,b = b,a
    if(a==1 or b==1):
        return True
    if(a == b or a%b==0):
        return False
    while(a%b != 0):
        a = a % b
        if(a<b):
            a,b = b,a
    return b == 1

a, b = map(int, input().split())
if(is_comprime(a,b)):
    print("YES")
else:
    print("NO")
