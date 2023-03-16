def is_comprime(a,b):
    pow2 = [2,4,8]
    if(a in pow2 and b%2!=0):
        return True
    if(b in pow2 and a%2!=0):
        return True
    if(a<b):
        a,b = b,a
    if(a == b or (a==1 or b==1) or a%b==0):
        return False
    while(a!=b):
        a = a-b
        if(a<b): a,b = b,a
    return a == 1 and b == 1

a, b = map(int, input().split())
if(is_comprime(a,b)):
    print("YES")
else:
    print("NO")
