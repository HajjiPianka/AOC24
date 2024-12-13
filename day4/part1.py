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
for i in range(len(data[0])): #for every column
    for j in range(len(data)-4): #rows
        c1, c2, c3, c4 = data[j][i], data[j+1][i], data[j+2][i], data[j+3][i]
        word = c1 + c2 + c3 + c4
        if word == 'XMAS' or word == 'SAMX':
            answer += 1