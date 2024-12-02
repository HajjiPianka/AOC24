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


