file = open('data.txt','r')
data = file.readlines()
file.close()
rules = []
i = 1
for row in data:
    i+= 1
    row = row.strip()
    print(i)
    if row.count('|'): #its a rule
        values = row.split('|')
        rules.append(values)
    else: #updates
        ...