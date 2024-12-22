file = open('data.txt','r')
map = file.readlines()
file.close()

visitedCount = 0
x, y = 73, 94 #starting position

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