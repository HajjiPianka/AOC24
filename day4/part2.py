file = open('data.txt','r')
data = file.readlines()
file.close()

answer = 0

for i in range(1,len(data)-1): #skip first and last row, looking just middle ones (letter A)
    line = data[i].strip()
    for index in range(1,len(line)-1): #skip first and last letter to not get out of range
        char = line[index]
        if char == 'A':
            chars = [data[i-1][index-1], data[i-1][index+1], data[i+1][index-1], data[i+1][index+1]] #check chars diagonal to 'A'
            if chars.count('M') == 2 and chars.count('S') == 2:
                answer += 1 
                
print(answer)