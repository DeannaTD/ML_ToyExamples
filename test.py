import random
import os
os.system('pip install keyboard')
import keyboard
import time

stop = False

def printMaze(maze):
    os.system('cls')
    for row in maze:
        for cell in row:
            if(cell == 1):
                print(wall, end="")
            elif(cell == 0):
                print(" ", end="")
            elif(cell == 2):
                print(player, end="")
            elif(cell == 4):
                print("X", end="")
        print()

def updateMaze(prev, current):
    if(stop):
        return
    x = prev[0]
    y = prev[1]
    print("\033[%d;%dH" % (x + 1, y + 1), end = "")
    print(" ", end="")
    x = current[0]
    y = current[1]
    print("\033[%d;%dH" % (x + 1, y + 1), end = "")
    print(player, end="")
    print("\033[%d;%dH" % (N+1, N+1), end = "")
    print(" ")

def ContainsEmpty(visited):
    for row in visited:
        for cell in row:
            if (not cell):
                return True
    return False

def moveLeft():
    if(current[1] - 1 < 0):
        return
    if(maze[current[0]][current[1] - 1] != 1):
        tprint = False
        prev = [current[0], current[1]]
        maze[current[0]][current[1]] = 0
        current[1] -= 1
        maze[current[0]][current[1]] = 2
        updateMaze(prev, current)
        pX = current[0]
        pY = current[1]
        pathway.append([pX, pY])
        tprint = True

def moveRight():
    if(current[1] + 1 >= N):
        return
    if(maze[current[0]][current[1] + 1] != 1):
        tprint = False
        prev = [current[0], current[1]]
        maze[current[0]][current[1]] = 0
        current[1] += 1
        maze[current[0]][current[1]] = 2
        updateMaze(prev, current)
        pX = current[0]
        pY = current[1]
        pathway.append([pX, pY])
        tprint = True

def moveUp():
    if (current[0] - 1 <= 0):
        return
    if(maze[current[0] - 1][current[1]] != 1):
        tprint = False
        prev = [current[0], current[1]]
        maze[current[0]][current[1]] = 0
        current[0] -= 1
        maze[current[0]][current[1]] = 2
        updateMaze(prev, current)
        pX = current[0]
        pY = current[1]
        pathway.append([pX, pY])
        tprint = True

def moveDown():
    if (current[0] + 1 >= N):
        return
    if(maze[current[0] + 1][current[1]] != 1):
        tprint = False
        prev = [current[0], current[1]]
        maze[current[0]][current[1]] = 0
        current[0] += 1
        maze[current[0]][current[1]] = 2
        updateMaze(prev, current)
        pX = current[0]
        pY = current[1]
        pathway.append([pX, pY])
        tprint = True

def getRandomTrue(arr):
    ind = []
    for i in range(len(arr)):
        if(arr[i]):
            ind.append(i)
    result = random.randint(0, len(ind) - 1)
    return ind[result]

def quitGame():
    exit()

start = """
    --------------------------------------------
   ///    ____   _____    _     __   _____   ///
    ///  |____     |     /_\   |__|    |      ///
     ///  ____|    |    /   \  |  \    |       ///
     ----------------------------------------------
                Press Enter key to start
"""

print(start)
input()

print("Choose difficulty:")
print("1 - Easy")
print("2 - Medium")
print("3 - Hard")
print("4 - Extreme")
print("5 - Custom")

diff = 0

while(diff > 5 or diff < 1):
    diff = input(">> ")
    if(diff != ""):
        diff = int(diff)
        if(diff > 5 or diff < 1):
            print("Choose difficulty again")
    else:
        diff = 0

N = 15

if(diff == 1):
    N = 9
    f = 3
elif(diff == 2):
    N = 15
    f = 5
elif(diff == 3):
    N = 19
    f = 7
elif(diff == 4):
    N = 25
    f = 9
elif(diff == 5):
    print("Maze size: >>")
    N = int(input())
    if(N % 2 == 0):
        N += 1
    print("Flags count: >>")
    f = int(input())
    
timeDiff = 0

print("Choose time difficulty:")
print("1 - Easy")
print("2 - Medium")
print("3 - Hard")
print("4 - Extreme")

while(timeDiff > 4 or timeDiff < 1):
    timeDiff = input(">> ")
    if(timeDiff != ""):
        timeDiff = int(timeDiff)
        if(timeDiff > 4 or timeDiff < 1):
            print("Choose difficulty again")
    else:
        timeDiff = 0


if(timeDiff == 1):
    timeDiff = 120
elif(timeDiff == 2):
    timeDiff = 60
elif(timeDiff == 3):
    timeDiff = 30
elif(timeDiff == 4):
    timeDiff = 20

os.system('cls')
print("                      Rules                    ")
print("-----------------------------------------------")
print("Maze size: ", N, "x", N)
print("Collect", f, "flags X in ", timeDiff, " seconds")
print("Press 'a' to move left")
print("Press 'd' to move right")
print("Press 'w' to move up")
print("Press 's' to move down")
print("Press 'q' to quit")
print("-----------------------------------------------")
print("Press Enter to start game")
input()

maze = []
visited = []
path = [] #Стек
current = [1,1]
tprint = True
pathc = "∘" #знак для вывода пути
wall = "█"
player = "\U00013020"
pathway = [] #массив пути

pathway.append(current)

for i in range(N):
    row = []
    rowp = []
    if(i % 2 == 0):
        for j in range(N):
            row.append(1)
            rowp.append(True)
    else:
        for j in range(N):
            if(j % 2 == 0):
                row.append(1)
                rowp.append(True)
            else:
                row.append(0)
                rowp.append(False)
    visited.append(rowp)
    maze.append(row)

visited[current[0]][current[1]] = True

while(ContainsEmpty(visited)):
    x = current[0]
    y = current[1]
    t = []
    if(x - 2 >= 0):
        if(visited[x-2][y] == False):
            t.append(True)
        else:
            t.append(False)
    else:
        t.append(False)
    if(x + 2 < N):
        if(visited[x+2][y] == False):
            t.append(True)
        else:
            t.append(False)
    else:
        t.append(False)
    if(y - 2 >= 0):
        if(visited[x][y-2] == False):
            t.append(True)
        else:
            t.append(False)
    else:
        t.append(False)
    if(y + 2 < N):
        if(visited[x][y+2] == False):
            t.append(True)
        else:
            t.append(False)
    else:
        t.append(False)
    if(True in t):
        path.append(current)
        nextr = getRandomTrue(t)
        if(nextr == 0):
            current = [x-2, y]
            maze[x-1][y] = 0
        elif(nextr == 1):
            current = [x+2, y]
            maze[x+1][y] = 0
        elif(nextr == 2):
            current = [x, y-2]
            maze[x][y-1] = 0
        elif(nextr == 3):
            current = [x, y+2]
            maze[x][y+1] = 0
        visited[current[0]][current[1]] = True
    elif(len(path) > 0):
        current = path.pop()

maze[1][0] = 0
maze[N-2][N-1] = 0

current = [1,0]
maze[current[0]][current[1]] = 2

while(f > 0):
    x = random.randint(0, N - 1)
    y = random.randint(0, N - 1)
    if(maze[x][y] == 0):
        maze[x][y] = 4
        f -= 1

timeStart = time.time()
timeNow = time.time()

keyboard.add_hotkey('a', moveLeft)
keyboard.add_hotkey('d', moveRight)
keyboard.add_hotkey('w', moveUp)
keyboard.add_hotkey('s', moveDown)
keyboard.add_hotkey('q', quitGame)

printMaze(maze)

win = """
     ----------------------------------------------------------------------------------------------------
     |||                            _____                                  _______                    |||
     |||      /\    /\     |    |  |     |  |    |     \      /\      /       |      |\   |     |     |||
     |||                   |____|  |     |  |    |      \    /  \    /        |      | \  |     |     |||
     |||       \____/           |  |     |  |    |       \  /    \  /         |      |  \ |     |     |||
     |||                   |____|  |_____|  |____|        \/      \/       ___|___   |   \|     .     |||
     ----------------------------------------------------------------------------------------------------
"""

lose = """
     ---------------------------------------------------------------------------------------------
     |||                            _____                      _____    _____    _____
     |||      /\    /\     |    |  |     |  |    |    |       |     |  |        |
     |||        ____       |____|  |     |  |    |    |       |     |  |_____   |_____
     |||       /    \           |  |     |  |    |    |     _ |     |        |  |
     |||                   |____|  |_____|  |____|    |_____| |_____|  ______|  |_____   . . .  


                           ____    _____    ____      ____
                          |       |     |  |    |    |    |    |    |                           |||
                          |____   |     |  |____|    |____|    |____|                           |||  
                               |  |     |  |    \    |    \         |                           |||
                           ____|  |_____|  |     \   |     \   |____| . . .                     |||
    --------------------------------------------------------------------------------------------|||
"""

while(current != [N-2, N-1] and timeNow - timeStart < timeDiff):
    timeNow = time.time()
    if(tprint and abs(timeNow - int(timeNow)) < 0.01):
        print("\033[%d;%dH" % (0, N + 3), end = "")
        print("Time: ", timeDiff - int(timeNow - timeStart), "s", end = "")

for i in pathway:
    pX = i[0]
    pY = i[1]
    maze[pX][pY] = 3

fleft = 0

if(current == [N-2, N-1]):
    for row in maze:
        for cell in row:
            if(cell == 4):
                fleft += 1
    if(fleft == 0):
        os.system('cls')
        print(win)
        for i in range(N):
            for j in range(N):
                if(maze[i][j] == 1):
                    print(wall, end="")
                elif(maze[i][j] == 0):
                    print(" ", end="")
                elif(maze[i][j] == 2):
                    print(player, end="")
                elif(maze[i][j] == 3):
                    print(pathc, end="")
            print()
    else:
        os.system('cls')
        print(lose)
        for i in range(N):
            for j in range(N):
                if(maze[i][j] == 1):
                    print(wall, end="")
                elif(maze[i][j] == 0):
                    print(" ", end="")
                elif(maze[i][j] == 2):
                    print(player, end="")
                elif(maze[i][j] == 3):
                    print(pathc, end="")
                elif(maze[i][j] == 4):
                    print("X", end="")
            print()
        print("Flags left: ", fleft)
else:
    os.system('cls')
    print(lose)
    for i in range(N):
        for j in range(N):
            if(maze[i][j] == 1):
                print(wall, end="")
            elif(maze[i][j] == 0):
                print(" ", end="")
            elif(maze[i][j] == 2):
                print(player, end="")
            elif(maze[i][j] == 3):
                print(pathc, end="")
        print()
