#read data
file = open('data.txt','r')
data = file.readlines()
file.close()

partSafe = []
#remove rows that aren't all increasing or all decreasing
for row in data:
    row = list(map(int, row.strip().split()))
    #check if all increases
    if sorted(row) == row:
        partSafe.append(row)
    #check if all decreasing
    elif sorted(row, reverse=True) == row:
        partSafe.append(row)

#check difference between elements
def smallDifference(row: list) -> bool:
    '''check if step between values is between 1 and 3'''

    #compare value with the next one
    for i in range(len(row)-1):
        diff = abs(row[i] - row[i+1]) #absolute value in case of increasing 
        if diff == 0 or diff > 3: #if slope too high or values equal
            return False
    return True

#count safe rows
safeRows = []
for row in partSafe:
    if smallDifference(row):
        safeRows.append(row)

print(len(safeRows))