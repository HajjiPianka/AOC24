#read data
file = open('data.txt','r')
data = file.readlines()
file.close()

def check_row(row):
    diffs = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if (all(x < 0 and x in range(-3, 0) for x in diffs) or all(x > 0 and x in range(1, 4) for x in diffs)): # all differences in (1,3) or (-3,-1)
        return True
    return False

safe = 0

for line in data:
    levels = [int(num.strip()) for num in line.split()]
    if check_row(levels):
        safe += 1
    else:
        for i in range(len(levels)): #check if removing single item fixes row
            levels2 = levels.copy()
            levels2.pop(i)
            if check_row(levels2):
                safe += 1
                break #no point in looking more
print(safe)