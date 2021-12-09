with open("C:/Users/Aditya/OneDrive/Desktop/Advent Of Code/day7.txt") as f:
    lis = f.read().split(',')
for i in range(len(lis)):
    lis[i]=int(lis[i])
mean = round(sum(lis)/len(lis))
fuel = 0
for i in lis:
    sum = 0
    diff = abs(i-mean)
    sum = (diff*(diff+1))//2
    fuel += sum
print(int(fuel)//10)
