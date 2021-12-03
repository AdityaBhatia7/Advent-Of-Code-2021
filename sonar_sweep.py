with open("C:/Users/Aditya/OneDrive/Desktop/values.txt") as f:
    lines = f.read().splitlines()
count = 0
for i in range(len(lines)-1):
    if int(lines[i+1]) > int(lines[i]):
        count += 1
print(count)
