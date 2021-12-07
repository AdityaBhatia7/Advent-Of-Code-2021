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
        if ((lines[x][0][0]==lines[x][1][0]) or (lines[x][0][1]==lines[x][1][1])):
            cord.append(lines[x])
    for i in range(len(cord)):
        if (cord[i][0][0]==cord[i][1][0]):
            maxi = max(int(cord[i][0][1]),int(cord[i][1][1]))
            mini = min(int(cord[i][0][1]),int(cord[i][1][1]))
            for m in range(mini, maxi+1):
                map[m][int(cord[i][0][0])] += 1
        else:
            maxi = max(int(cord[i][0][0]),int(cord[i][1][0]))
            mini = min(int(cord[i][0][0]),int(cord[i][1][0]))
            for n in range(mini, maxi+1):
                map[int(cord[i][0][1])][n] += 1
    count = 0
    for a in range(len(map)):
        for b in range(len(map[a])):
            if map[a][b] > 1:
                count +=1                            
    return count
print(main())
