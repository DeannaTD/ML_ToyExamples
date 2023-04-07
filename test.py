N = int(input())
A, B = map(int, input().split())

res = 0

for i in range(N):
    p = int(input())
    if A <= p <= B:
        res += 1

print(res)
