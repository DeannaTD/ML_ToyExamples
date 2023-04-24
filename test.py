N = str(int(input()))
if(len(N) % 2 == 1):
    print("unlucky")
else:
    m = len(N) // 2
    if(sum(map(int, N[:m])) == sum(map(int, N[m:]))):
        print("lucky")
    else:
        print("unlucky")
