import math
numbers = map(float, input().split())
s = sum(numbers)

if s == math.floor(s):
    print(int(s))
else: 
    print(s)
