import random
def printArray(array):
    for i in range(len(array)-1):
        print(array[i], end=" ")
    print(array[len(array)-1])

N = int(input())

arr = []

for i in range(N):
    arr.append(random.randint(0,5))

printArray(arr)

f = False
for i in range(N):
    if (arr.count(arr[i]) > 1):
        if(not f):
            print("YES")
            f = True
        print(i)
if(not f):
    print("NO")
