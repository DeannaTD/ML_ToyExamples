N = int(input())
A = []

for i in range(N):
    A.append(input())

ans = 2**63
mz = 0

for a in A:
    zeroes = 0
    for i in range(len(a) - 1, -1, -1):
        if(a[i] == '0'):
            zeroes += 1
        else: 
            break
    if(zeroes > mz):
        ans = a
        mz = zeroes
    elif(zeroes == mz):
        ans = str(min(int(ans), int(a)))
print(ans)
