with open("C:/Users/Aditya/OneDrive/Desktop/Advent Of Code/day5.txt") as f:
    lines = f.read().splitlines()
newlines=[]
for i in range(len(lines)):
    lines[i] = str(lines[i])
cord = []
map = []
for x in range(1000):
    mapTemp = []
    for y in range(1000):
        mapTemp.append(0)
    map.append(mapTemp)
for j in range(len(lines)):
    lines[j] = lines[j].split(" -> ")
for m in range(len(lines)):
    for l in range(2):
        lines[m][l] = lines[m][l].split(',')
def main():
    for x in range(len(lines)):
        if (int(lines[x][1][0])-int(lines[x][0][0])) != 0:
            slope = (int(lines[x][1][1])-int(lines[x][0][1]))/(int(lines[x][1][0])-int(lines[x][0][0]))
        else:
            slope = 0
        if ((lines[x][0][0]==lines[x][1][0]) or (lines[x][0][1]==lines[x][1][1]) or slope == 1 or slope == -1):
            cord.append(lines[x])
    for i in range(len(cord)):
        if (cord[i][0][0]==cord[i][1][0]):
            maxi = max(int(cord[i][0][1]),int(cord[i][1][1]))
            mini = min(int(cord[i][0][1]),int(cord[i][1][1]))
            for m in range(mini, maxi+1):
                map[m][int(cord[i][0][0])] += 1
                
        elif (cord[i][0][1]==cord[i][1][1]):
            maxi = max(int(cord[i][0][0]),int(cord[i][1][0]))
            mini = min(int(cord[i][0][0]),int(cord[i][1][0]))
            for n in range(mini, maxi+1):
                map[int(cord[i][0][1])][n] += 1
        
        else:
            xStep = 1 if (int(cord[i][1][0]) - int(cord[i][0][0])) > 0 else -1
            yStep = 1 if (int(cord[i][1][1]) - int(cord[i][0][1])) > 0 else -1
            for step in range(0,abs(int(cord[i][1][0]) - int(cord[i][0][0]))):
                map[int(cord[i][0][1]) + step*yStep][int(cord[i][0][0]) + step*xStep] += 1
            map[int(cord[i][1][1])][int(cord[i][1][0])] += 1

                
    count = 0
    for a in range(len(map)):
        for b in range(len(map[a])):
            if map[a][b] > 1:
                count +=1                            
    return count

print(main())
