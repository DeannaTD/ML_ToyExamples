def Nor(x,y):
    if (x == 0 and y == 0):
        return 1
    return 0


N = int(input())
a = []
for i in range(N):
    x,y = map(int, input().split())
    a.append(Nor(x,y))

for i in a:
    print(i)
