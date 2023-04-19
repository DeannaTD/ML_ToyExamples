number = input()

result = ""
for i in range(1, len(number)-1):
    result += number[i]

if(int(result) == 0):
    print(int(result))
else:
    print("")
