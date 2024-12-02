#read data
file = open('data.txt','r')
data = file.readlines()
file.close()


#split data into two arrays
left = []
right = []

for row in data:
    #strip row and split into columns
    row = row.strip().split('   ')

    #to make sorting easier parse value to int
    left.append(int(row[0]))
    right.append(int(row[1]))

#sort arrays in ascending order
left.sort()
right.sort()

#calculate and sum differences between coresponding values
differenceSum = 0
for i in range(len(left)):
    # get absolute value if left is smaller than right 
    difference = abs(left[i] - right[i])

    #add to sum
    differenceSum += difference

#get the answer
print(differenceSum)