file = open('data.txt','r')
data = file.readlines()
file.close()

answer = 0

for i in range(1,len(data)-1): #skip first and last row, looking just middle ones (letter A)
    line = data[i].strip()
    for index in range(1,len(line)-1): #skip first and last letter to not get out of range
        char = line[index]
        if char == 'A':
            diag1 = data[i-1][index-1] + 'A' + data[i+1][index+1] #first diagonal
            diag2 = data[i-1][index+1] + 'A' + data[i+1][index-1] #second diagonal
            if diag1 == 'MAS' or diag1 == 'SAM':
                if diag2 == 'MAS' or diag2 == 'SAM':
                    answer += 1
                
print(answer)