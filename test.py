k = int(input())
s = input()

if(k<0):
    s = s[::-1]
    k *= -1
    
print(s * k)
