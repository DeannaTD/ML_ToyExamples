def Election(x,y,z):
    if(x + y + z > 1):
        return 1
    else:
        return 0

N = int(input())
a = []
for i in range(N):
    x,y,z = map(int, input().split())
    a.append(Election(x,y,z))

for i in a:
    print(i)
