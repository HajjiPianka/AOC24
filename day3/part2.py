file = open('data.txt','r')
data = file.readlines()
file.close()

answer = 0
flag = 1 #enabled by default
enabledInstructions = []
for line in data:
    doOrNot = line.strip().split("do")
    for checkedLine in doOrNot:
        if checkedLine.startswith('()'):
            flag = 1
        if checkedLine.startswith('n\'t()'):
            flag = 0
        
        if flag:
            enabledInstructions.append(checkedLine)

for line in enabledInstructions:
    starts = line.strip().split('mul(')[1:] #beginnings of mul instructions, skip chars before first instruction
    for instruction in starts:
        instruction = instruction.split(')') #remove chars after instruction
        if len(instruction) == 1:
            continue #not a real instruction, go next
        instruction = instruction[0] #before closing bracket
        values = instruction.split(',')
        if len(values) != 2:
            continue #not a real instruction, go next
        try:
            value1 = int(values[0])
            value2 = int(values[1])
        except:
            continue #not a real instruction, go next
        operation = value1 * value2
        answer += operation
print(answer)