with open("C:/Users/Aditya/OneDrive/Desktop/Advent Of Code/day6.txt") as f:
    fishes = f.read().split(',')
    
for a in range(len(fishes)):
    fishes[a] = int(fishes[a])
    
def main(days):
    for i in range(days):
        for x in range(len(fishes)):
            if fishes[x] == 0:
                fishes[x] = 6
                fishes.append(8)
            else:
                fishes[x] -= 1
    return(len(fishes))
        
print(main(80))
