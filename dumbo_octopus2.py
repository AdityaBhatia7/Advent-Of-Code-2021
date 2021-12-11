with open('C:/Users/Aditya/OneDrive/Desktop/Advent Of Code/day11.txt') as f:
    lines = f.read().splitlines()
for i in range(len(lines)):
    lines[i] = list(lines[i])
for i in range(len(lines)):
    for j in range(len(lines[i])):
        lines[i][j] = int(lines[i][j])
def explode(a,b,lines,checked):
    if a < 0 or b < 0 or a >= len(lines) or b >= len(lines):
        return 0
    if lines[a][b] == 0:
        return 0
    if (a,b) in checked:
        checked.remove((a,b))
    else:
        lines[a][b] += 1
    if lines[a][b] > 9:
        lines[a][b] = 0
        c = 1+explode(a-1,b-1,lines,checked)+explode(a-1,b,lines,checked)+explode(a-1,b+1,lines,checked)+explode(a,b-1,lines,checked)+explode(a,b+1,lines,checked)+explode(a+1,b-1,lines,checked)+explode(a+1,b,lines,checked)+explode(a+1,b+1,lines,checked)
        return c
    else:
        return 0   
def flash(n):
    for a in range(n):
        count = 0
        checked=[]
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                lines[i][j] += 1
                checked.append((i,j))
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                count += explode(i,j,lines,checked)
        if count == (len(lines)**2):
            return a+1   
print(flash(1000))  
