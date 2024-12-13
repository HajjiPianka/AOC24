file = open('data.txt','r')
data = file.readlines()
file.close()

normal = 0
reverse = 0 

for line in data:
    line = line.strip()
    for i in range(len(line)-3):
        word = line[i] + line[i+1] + line[i+2] + line[i+3]
        if word == 'XMAS':
            normal += 1
        elif word == 'SAMX':
            reverse += 1