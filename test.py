def shiftSum(a, b, s):
    if(a == '1' and b == '1'): return True
    if(a == '0' and b == '0'): return False
    return s

a, b = input().split()
s = False
c = 0
if(len(a) > len(b)):
    b = b.zfill(len(a))
elif(len(b) > len(a)):
    a = a.zfill(len(b))

for i in range(len(a)-1, -1, -1):
    s = shiftSum(a[i], b[i], s)
    if(s): c += 1

print(c+1)
