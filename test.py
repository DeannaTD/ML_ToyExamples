import math

N = int(input())
numbers = map(int, input().split())

res = 0

for n in numbers:
    res += n

print(math.floor(res / N))
