N = int(input())
A, B = map(int, input().split())
players = map(int, input().split())

res = 0

for p in players:
    if A <= p <= B:
        res += 1

print(res)
