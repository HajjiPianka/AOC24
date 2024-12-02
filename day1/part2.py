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

totalScore = 0
#calculate similarity score for each value in left array
for valueL in left:
    #count apperances of left value in right array
    count = 0
    for valueR in right:
        if valueL == valueR:
            count += 1
    #calculate score for this value
    score = valueL * count
    #add to total score
    totalScore += score
    