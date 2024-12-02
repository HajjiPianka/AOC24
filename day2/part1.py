#read data
file = open('data.txt','r')
data = file.readlines()
file.close()

partSafe = []
#remove rows that aren't all increasing or all decreasing
for row in data:
    row = row.strip().split(' ')
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
        diff = abs(row[i] - row[i]) #absolute value in case of increasing 
        if diff == 0 or diff > 3:
            return False
    return True
