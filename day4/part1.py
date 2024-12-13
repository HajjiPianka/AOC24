file = open('data.txt','r')
data = file.readlines()
file.close()

answer = 0

for line in data:
    line = line.strip()
    for i in range(len(line)-3): #normal and reversed in line
        word = line[i] + line[i+1] + line[i+2] + line[i+3]
        if word == 'XMAS' or word == 'SAMX':
            answer += 1
#vertical
for i in range(len(data)-3): #rows
    for j in range(len(data[i])-1): #column
        c1, c2, c3, c4 = data[i][j], data[i+1][j], data[i+2][j], data[i+3][j] #chars
        word = c1 + c2 + c3 + c4
        if word == 'XMAS' or word == 'SAMX':
            answer += 1
#diagonal
for i in range(len(data)-3): #row
    for j in range(len(data[i])-4): #column
        print(f'i: {i} j: {j}')
        c1, c2, c3, c4 = data[i][j], data[i+1][j+1], data[i+2][j+2], data[i+3][j+3] #first diagonal
        word = c1 + c2 + c3 + c4
        if word == 'XMAS' or word == 'SAMX':
            answer += 1
        c1, c2, c3, c4 = data[i+3][j], data[i+2][j+1], data[i+1][j+2], data[i][j+3] #second diagonal
        word = c1 + c2 + c3 + c4
        if word == 'XMAS' or word == 'SAMX':
            answer += 1
print(answer)