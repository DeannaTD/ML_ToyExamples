s = input()
sign = ""
t = []
if(s.__contains__("+")):
    sign = "+"
    t = s.split("+")
else:
    sign = "-"
    t = s.split("-")

if(sign == "+"):
    print(int(t[0]) + int(t[1]))
else:
    print(int(t[0]) - int(t[1]))
