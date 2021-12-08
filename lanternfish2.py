with open("C:/Users/Aditya/OneDrive/Desktop/Advent Of Code/day6.txt") as f:
    fishes = f.read().split(',')
fishesNew = {}
days = int(input("Enter number of days: "))   
for a in range(len(fishes)):
    fishes[a] = int(fishes[a])
for b in range(9):
    fishesNew.update({str(b):fishes.count(b)}) 
    
def main(fishes):
    tempFishes = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}
    for j in range(9):
        if j == 6:
            tempFishes[str(j)] += fishes.get('0')
            tempFishes[str(j)] += fishes.get(str(j+1))
            
        elif j == 8:
            tempFishes[str(j)] += fishes.get('0')
                    
        else:
            tempFishes[str(j)] += fishes.get(str(j+1))

    return tempFishes
        
for i in range(days):
    fishesNew = main(fishesNew)
sum = 0
for i in fishesNew:
    sum += fishesNew[i]
print(sum)
