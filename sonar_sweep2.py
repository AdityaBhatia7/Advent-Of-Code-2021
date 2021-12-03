with open("C:/Users/Aditya/OneDrive/Desktop/values.txt") as f:
    lines = f.read().splitlines()
count = 0
for i in range(len(lines)):
    lines[i] = int(lines[i])
for i in range(len(lines)-3):
    sum1 = lines[i] + lines[i+1] + lines[i+2]
    sum2 = lines[i+1] + lines[i+2] + lines[i+3]
    if sum2 > sum1:
        count += 1
print(count)
