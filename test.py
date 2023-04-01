import random

N, X = map(int, input().split())
A = []
ans = []
for i in range(N):
    A.append(random.randint(0, 5))
    if(A[i] == X):
        ans.append(i)

print(" ".join(map(str, A)))
for a in ans:
    print(a)
