file = open('data.txt','r')
map = file.readlines()
file.close()

class Guard:
    def __init__(self, posX, posY, facing):
        self.posX = posX
        self.posY = posY
        self.facing = facing
        self.isOnMap = True
        self.visitedTiles = 0
    def turnRight(self):
        match self.facing:
            case '^':
                self.facing = '>'
            case '>':
                self.facing = 'v'
            case 'v':
                self.facing = '<'
            case '<':
                self.facing = '^'
    def forward(self):
        match self.facing:
            case '^':
                self.posY -= 1
            case '>':
                self.posX += 1
            case 'v':
                self.posY += 1
            case '<':
                self.posX -= 1
    def newTile(self):
        self.visitedTiles += 1

x, y = 73, 94 #starting position
guard = Guard(x, y, '^')

def isBlockadeAhead(guard: Guard):
    checkX, checkY = guard.posX, guard.posY
    #where to look
    if guard.facing == '<':
        checkX -= 1
    elif guard.facing == '>':
        checkX += 1
    elif guard.facing == 'v':
        checkY += 1
    else:
        checkY -= 1
    
    if map[checkX][checkY] == '#':
        return True
    return False

def isGuardGonnaLeave(guard: Guard):
    maxX = len(map[0]) - 1
    maxY = len(map) - 2 #empty row at the end of data file
    posX, posY = guard.posX, guard.posY
    match guard.facing:
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

while (guard.isOnMap):
    #is guard on a new tile
    if map[y][x] == '.': #row then column
        guard.newTile()
        map[y][x] = 'X'
    if isBlockadeAhead(guard):
        ...