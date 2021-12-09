with open("C:/Users/Aditya/OneDrive/Desktop/Advent Of Code/day9.txt") as f:
    lines = f.read().splitlines()
for i in range(len(lines)):
    lines[i] = list((lines[i]))
for i in range(len(lines)):
    for j in range(len(lines[i])):
        lines[i][j]= int(lines[i][j])
def main():
    lis=[]
    for i in range(len(lines)):
        if i == 0:
            for j in range(len(lines[i])):
                if j == 0:
                    if lines[i][j] == min(lines[i][j],lines[i+1][j],lines[i][j+1]) and lines[i][j] != 9:
                        lis.append(lines[i][j])
                elif j == len(lines[i])-1:
                    if lines[i][j] == min(lines[i][j],lines[i+1][j],lines[i][j-1]) and lines[i][j] != 9:
                        lis.append(lines[i][j])
                else:
                    if lines[i][j] == min(lines[i][j],lines[i+1][j],lines[i][j-1],lines[i][j+1]) and lines[i][j] != 9:
                        lis.append(lines[i][j])
        elif i == len(lines)-1:
            for j in range(len(lines[i])):
                if j == 0:
                    if lines[i][j] == min(lines[i][j],lines[i-1][j],lines[i][j+1]) and lines[i][j] != 9:
                        lis.append(lines[i][j])
                elif j == len(lines[i])-1:
                    if lines[i][j] == min(lines[i][j],lines[i-1][j],lines[i][j-1]) and lines[i][j] != 9:
                        lis.append(lines[i][j])
                else:
                    if lines[i][j] == min(lines[i][j],lines[i-1][j],lines[i][j-1],lines[i][j+1]) and lines[i][j] != 9:
                        lis.append(lines[i][j])
        else:
            for j in range(len(lines[i])):
                if j == 0:
                    if lines[i][j] == min(lines[i][j],lines[i-1][j],lines[i+1][j],lines[i][j+1]) and lines[i][j] != 9:
                        lis.append(lines[i][j])
                elif j == len(lines[i])-1:
                    if lines[i][j] == min(lines[i][j],lines[i-1][j],lines[i+1][j],lines[i][j-1]) and lines[i][j] != 9:
                        lis.append(lines[i][j])
                else:
                    if lines[i][j] == min(lines[i][j],lines[i-1][j],lines[i+1][j],lines[i][j-1],lines[i][j+1]) and lines[i][j] != 9:
                        lis.append(lines[i][j])
    print(lis)
    Sum = sum(lis) + len(lis)
    return Sum

print(main())
