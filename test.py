number = input()

result = ""
for i in range(1, len(number)-1):
    result += number[i]

print(int(result))
