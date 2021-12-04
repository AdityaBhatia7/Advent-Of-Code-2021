with open("C:/Users/Aditya/OneDrive/Desktop/Advent Of Code/day3.txt") as f:
    lines = f.read().splitlines()
gamma_rate = ""
epsilon_rate = ""
count0 = 0
count1 = 0
for i in range(len(lines[1])):
    for j in range(len(lines)):
        if lines[j][i]=="0":
            count0 += 1
        else:
            count1 += 1
    if count0 > count1:
        gamma_rate += "0"
        epsilon_rate += "1"
    else:
        gamma_rate += "1"
        epsilon_rate += "0"
    count0 = 0
    count1 = 0
print(int(gamma_rate,2)*int(epsilon_rate,2))
