import random
import os
#os.system('pip install keyboard')
import keyboard

def printMaze(maze):
    os.system('cls')
    for row in maze:
        for cell in row:
            if(cell == 1):
                print("█", end="")
            elif(cell == 0):
                print(" ", end="")
            elif(cell == 2):
                print("O", end="")
        print()

def ContainsEmpty(visited):
    for row in visited:
        if(False in row):
            return True
    return False

maze = []
visited = []
N = 15
path = [] #Стек
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


current = [1,1]
visited[current[0]][current[1]] = True

def getRandomTrue(arr):
    ind = []
    for i in range(len(arr)):
        if(arr[i]):
            ind.append(i)
    return ind[random.randint(0, len(ind) - 1)]


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
printMaze(maze)

def updateMaze(prev, current):
    x = prev[0]
    y = prev[1]
    print("\033[%d;%dH" % (x + 1, y + 1), end = "")
    print(" ", end="")
    x = current[0]
    y = current[1]
    print("\033[%d;%dH" % (x + 1, y + 1), end = "")
    print("O", end="")
    print("\033[%d;%dH" % (N+5, N+5), end = "")
    print(" ")

def moveLeft():
    if(current[1] - 1 >= 0):
        if(maze[current[0]][current[1] - 1] != 1):
            prev = [current[0], current[1]]
            maze[current[0]][current[1]] = 0
            current[1] -= 1
            maze[current[0]][current[1]] = 2
            updateMaze(prev, current)

def moveRight():
    if(current[1] + 1 < N):
        if(maze[current[0]][current[1] + 1] != 1):
            prev = [current[0], current[1]]
            maze[current[0]][current[1]] = 0
            current[1] += 1
            maze[current[0]][current[1]] = 2
            updateMaze(prev, current)

def moveUp():
    if(maze[current[0] - 1][current[1]] != 1):
        prev = [current[0], current[1]]
        maze[current[0]][current[1]] = 0
        current[0] -= 1
        maze[current[0]][current[1]] = 2
        updateMaze(prev, current)

def moveDown():
    if(maze[current[0] + 1][current[1]] != 1):
        prev = [current[0], current[1]]
        maze[current[0]][current[1]] = 0
        current[0] += 1
        maze[current[0]][current[1]] = 2
        updateMaze(prev, current)

keyboard.add_hotkey('a', moveLeft)
keyboard.add_hotkey('d', moveRight)
keyboard.add_hotkey('w', moveUp)
keyboard.add_hotkey('s', moveDown)

while(current != [N-2, N-1]):
    pass
