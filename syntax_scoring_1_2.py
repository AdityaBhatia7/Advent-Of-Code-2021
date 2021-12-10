tokenDict = { '{':'}', '[':']', '(':')', '<':'>' }
illegalScore = { ')': 3, ']': 57, '}': 1197, '>': 25137}
completeScore = { ')': 1, ']': 2, '}': 3, '>': 4 }
p1 = 0
startToken = tokenDict.keys()
scores = []

with open('C:/Users/Aditya/OneDrive/Desktop/Advent Of Code/day10.txt') as f:
    lines = f.read().splitlines()
for line in lines:
    stack = []
    illegalFound = False
    p2 = 0
    for i in line:
        if i in startToken:
            stack.append(i)
        else:
            if tokenDict[stack[-1]] != i:
                p1 += illegalScore[i]
                illegalFound = True
                break
            else:
                stack.pop()
    if not(illegalFound):
        while len(stack) != 0:
            p2 = p2*5 + completeScore[tokenDict[stack[-1]]]
            stack.pop()
        scores.append(p2)
        
print(p1)
print(sorted(scores)[len(scores)//2])
