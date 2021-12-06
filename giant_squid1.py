drawNums = (72,86,73,66,37,76,19,40,77,42,48,62,46,3,95,17,97,41,10,14,83,90,12,23,81,98,11,57,13,69,28,63,5,78,79,58,54,67,60,34,39,84,94,29,20,0,24,38,43,51,64,18,27,52,47,74,59,22,85,65,80,2,99,70,33,91,53,93,9,82,8,50,7,56,30,36,89,71,21,49,31,88,26,96,16,1,75,87,6,61,4,68,32,25,55,44,15,45,92,35)
with open("C:/Users/Aditya/OneDrive/Desktop/Advent Of Code/day4.txt") as f:
    boards = f.read().splitlines()
boardsNew = []
rem = []
for i in boards:
    if i=="":
        boards.remove(i)
for j in range(4,len(boards),5):
    boardsTemp = boards[j-4:j+1]
    boardsNew.append(boardsTemp)
for m in range(len(boardsNew)):
    for n in range(len(boardsNew[m])):
        boardsNew[m][n] = boardsNew[m][n].split(" ")
for x in range(len(boardsNew)):
    for y in range(len(boardsNew[x])):
        for z in range(len(boardsNew[x][y])):
            if boardsNew[x][y][z] == "":
                rem.append((x,y,z))
            if boardsNew[x][y][z] == "10\t\t":
                boardsNew[x][y][z] = "10"
for r in rem[::-1]:
    x,y,z = r
    del boardsNew[x][y][z]
    
br = False
for a in drawNums:
    if br == True:
        break
    else:
        for x in range(len(boardsNew)):
            for y in range(len(boardsNew[x])):
                for z in range(len(boardsNew[x][y])):
                    if a == int(boardsNew[x][y][z]):
                        boardsNew[x][y][z] = "111"

        for l in range(len(boardsNew)):
            if br == True:
                break    
            for s in range(5):
                if boardsNew[l][0] == ['111', '111', '111', '111', '111'] or boardsNew[l][1] == ['111', '111', '111', '111', '111'] or boardsNew[l][2] == ['111', '111', '111', '111', '111'] or boardsNew[l][3] == ['111', '111', '111', '111', '111'] or boardsNew[l][4] == ['111', '111', '111', '111', '111']:
                    br = True
                elif boardsNew[l][0][s] == "111" and boardsNew[l][1][s] == "111" and boardsNew[l][2][s] == "111" and boardsNew[l][3][s] == "111" and boardsNew[l][4][s] == "111":
                    br = True
                elif boardsNew[l][0][0] == "111" and boardsNew[l][1][1] == "111" and boardsNew[l][2][2] == "111" and boardsNew[l][3][3] == "111" and boardsNew[l][4][4] == "111":
                    br = True
                elif boardsNew[l][0][4] == "111" and boardsNew[l][1][3] == "111" and boardsNew[l][2][2] == "111" and boardsNew[l][3][1] == "111" and boardsNew[l][4][0] == "111":
                    br = True
for q in boardsNew[l-1]:
    print(q)
sum = 0
for f in boardsNew[l-1]:
    for t in f:
        if t != "111":
            sum+=int(t)
a = drawNums[drawNums.index(a) - 1]
print(a)
print(sum*a)
"""
for q in boardsNew:
    for r in q:
        print(r)
    print()
"""
