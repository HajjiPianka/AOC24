file = open('data.txt','r')
data = file.readlines()
file.close()
rules = []
for row in data:
    row = row.strip()
    if row.count('|'): #its a rule
        values = row.split('|')
        rules.append(values)
    else: #updates
        ...