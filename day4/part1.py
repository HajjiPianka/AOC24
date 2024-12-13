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