import random

N = int(input())
numbers = []

for i in range(N-1):
    numbers.append(random.randint(0, 5))
    print(numbers[i], end=" ")
numbers.append(random.randint(0, 5))
print(numbers[N-1])

f = False

i = 0
while(i < N - 1):
    if(numbers[i] == numbers[i+1]):
        if(not f):
            print("YES", end="")
            f = True
        print(" %d" % i, end="")
        while(numbers[i] == numbers[i+1]):
            print(" %d" % (i+1), end="")
            i += 1
            if(i == N - 1):
                break
    i += 1
if(not f):
    print("NO")
