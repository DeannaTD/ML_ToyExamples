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

inds = []

for i in range(N):
    if(i in inds):
        continue
    if (arr.count(arr[i]) > 1):
        for j in range(i, N):
            if(arr[i] == arr[j]):
                inds.append(j)

if(len(inds) == 0):
    print("NO")
else:
    print("YES")

for ind in inds:
    print(ind)
