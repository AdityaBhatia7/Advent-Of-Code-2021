with open("C:/Users/Aditya/OneDrive/Desktop/Advent Of Code/day2.txt") as f:
    lines = f.read().splitlines()
h_po = 0
v_po = 0
for i in range(len(lines)):
    if "forward" in lines[i]:
        h_po += int(lines[i][-1])
    elif "up" in lines[i]:
        v_po -= int(lines[i][-1])
    else:
        v_po += int(lines[i][-1])
print(h_po*v_po)
