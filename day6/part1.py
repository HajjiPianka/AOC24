file = open('data.txt','r')
map = file.readlines()
file.close()

visitedCount = 0
x, y = 73, 94 #starting position
hasGuardLeft = False

moves = ['^', '>', 'v', '<']

def isBlockadeAhead(currX, currY, facing):
    checkX, checkY = currX, currY
    #where to look
    if facing == '<':
        checkX -= 1
    elif facing == '>':
        checkX += 1
    elif facing == 'v':
        checkY += 1
    else:
        checkY -= 1
    
    if map[checkX][checkY] == '#':
        return True
    return False

def isGuardGonnaLeave(posX, posY, facing):
    maxX = len(map[0]) - 1
    maxY = len(map) - 2 #empty row at the end of data file
    match facing:
        case '^':
            posY -= 1
        case '>':
            posX += 1
        case 'v':
            posY += 1
        case '<':
            posX -= 1
    if posX > maxX or posX < 0:
        return True
    if posY > maxY or posY < 0:
        return True
    return False

