#read data
file = open('data.txt','r')
data = file.readlines()
file.close()

unsafeRows = []
partSafe = []
def isAlmostSorted(row: list) -> bool:
    '''check if row is sorted with ONE exception'''
    for removedLevelIndex in range(len(row)):
        newRow = row[:removedLevelIndex] + row[removedLevelIndex + 1:]
        if sorted(newRow) == newRow or sorted(newRow, reverse=True) == newRow:
            return True
    return False

#remove rows that aren't all increasing or all decreasing
for row in data:
    row = list(map(int, row.strip().split()))
    #check if all increases
    if sorted(row) == row:
        partSafe.append(row)
    #check if all decreasing
    elif sorted(row, reverse=True) == row:
        partSafe.append(row)
    elif isAlmostSorted(row):
        unsafeRows.append(row)

def smallDifferenceWithOutOneLevel(row: list) -> bool:
    '''check if removing a single level fixes the row'''
    for removedLevelIndex in range(len(row)): # remove a single level
        newRow = row[:removedLevelIndex] + row[removedLevelIndex + 1:]
        fixed = True # row is valid until its finds error
        for i in range(len(newRow)-1):
            diff = abs(newRow[i] - newRow[i+1]) #absolute value in case of increasing 
            if diff == 0 or diff > 3: # second wrong slope
                fixed = False # hasn't helped
                break
        if fixed: #it worked
            return True
    return False #still wrong
        

#check difference between elements
def smallDifference(row: list) -> bool:
    '''check if step between values is between 1 and 3'''

    #compare value with the next one
    for i in range(len(row)-1):
        diff = abs(row[i] - row[i+1]) #absolute value in case of increasing 
        if diff == 0 or diff > 3: #if slope too high or values equal
            unsafeRows.append(row)
            return False
    return True

#count safe rows
safeRows = []
for row in partSafe:
    if smallDifference(row):
        safeRows.append(row)
    else:
        unsafeRows.append(row)

#check bad rows if can be fixed
for row in unsafeRows:
    if smallDifferenceWithOutOneLevel(row):
        safeRows.append(row)

print(len(safeRows))