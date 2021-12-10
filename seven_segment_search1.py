lis =[]
with open("C:/Users/Aditya/OneDrive/Desktop/Advent Of Code/day8.txt") as f:
    lines = f.read().splitlines()
    for i in lines:
        j = (i[i.find('|')+1:len(i)+1])
        lis.append(j.strip())
for i in range(len(lis)):
    lis[i]=lis[i].split(" ")
count = 0
for i in range(len(lis)):
    for j in range(len(lis[i])):
        if str(len(lis[i][j])) in "2347":
            count += 1
print(count)
