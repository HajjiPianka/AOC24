file = open('data.txt','r')
data = file.readlines()
file.close()
rules = []
updates = []
for row in data:
    row = row.strip()
    if row.count('|'): #its a rule
        values = row.split('|')
        rules.append(values)
    elif row == '': #skip empty rows
        continue
    else: #updates
        values = row.split(',')
        updates.append(values)
