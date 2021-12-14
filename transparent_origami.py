ins = ('fold along x=655\n\
fold along y=447\n\
fold along x=327\n\
fold along y=223\n\
fold along x=163\n\
fold along y=111\n\
fold along x=81\n\
fold along y=55\n\
fold along x=40\n\
fold along y=27\n\
fold along y=13\n\
fold along y=6')
ins = ins.split('\n')
for i in range(len(ins)):
    ins[i] = ins[i][(ins[i].rfind("g ")+2):len(ins[i])]
    ins[i] = ins[i].split('=')
with open('C:/Users/Aditya/OneDrive/Desktop/Advent Of Code/day13.txt') as f:
    lines = f.read().splitlines()
    for i in range(len(lines)):
        lines[i] = lines[i].split(',')
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] = int(lines[i][j])
lis = []
for i in range(1500):
    li = []
    for j in range(1500):
        li.append('.')
    lis.append(li)
print(ins)

for i in range(len(lines)):
    lis[lines[i][1]][lines[i][0]] = '#'
    
def compareX(i,l1,l2):
    if len(l2)>=len(l1):
        l2 = list(l2[::-1])
        newLine = l2[::-1]
        for j in range(1,len(l1)+1):
            if newLine[-j] == '#' or l1[-j] == '#':
                newLine[-j] = '#'
        lis[i] = newLine
    else:
        newLine=l1
        l2 = l2[::-1]
        for j in range(1,len(l2)+1):
            if newLine[-j] == '#' or l2[-j] == '#':
                newLine[-j] = '#'
        lis[i] = newLine
        
        
def compareY(i,l1,l2):
    if len(l2)>=len(l1):
        l2 = list(l2[::-1])
        newLine = l2
        for j in range(1,len(l1)+1):
            if newLine[-j] == '#' or l1[-j] == '#':
                newLine[-j] = '#'
        lis[i] = newLine
    else:
        newLine=l1
        l2 = l2[::-1]
        for j in range(1,len(l2)+1):
            if newLine[-j] == '#' or l2[-j] == '#':
                newLine[-j] = '#'
        lis[i] = newLine
           
for l in ins:
    if l[0] == 'y':
        lis = list(zip(*lis))[::-1]
        for i in range(len(lis)):
            compareY(i,lis[i][0:int(l[1])],lis[i][int(l[1])+1:len(lis[i])])
        lis = list(zip(*lis[::-1]))
        
    else:
        for i in range(len(lis)):
            compareX(i,lis[i][0:int(l[1])],lis[i][int(l[1])+1:len(lis[i])]) 
count = 0
for i in lis:
    for j in i:
        if j == '#':
            count += 1
print(count)
print(len(lis))
