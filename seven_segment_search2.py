lis =[]
lisOutput = []
with open("C:/Users/Aditya/OneDrive/Desktop/Advent Of Code/day8.txt") as f:
    lines = f.read().splitlines()
    for i in lines:
        j = (i[:i.find('|')-1])
        lis.append(j.strip())
    for i in lines:
        j = (i[i.find('|')+1:len(i)+1])
        lisOutput.append(j.strip())
        
for i in range(len(lis)):
    lis[i]=lis[i].split(" ")
for i in range(len(lisOutput)):
    lisOutput[i]=lisOutput[i].split(" ")

def check(a,b):
    if len(a)-len(b)==1 or len(a)-len(b)==2 or len(a)==len(b):
        i = ""
        for j in a:
            if j not in b:
                i += j
        return i
    else:
        return "z"
def common(a,b):
    i = ""
    for j in a:
        if j in b:
            i += j
    return i
def key(v, dic):
    for key,value in dic.items():
        if v == value:
            return key
def findnum(strnum):
    if all(x in strnum for x in['to','bo','br','bl','tr','tl']):
        return 0
    elif all(x in strnum for x in['to','bo','br','ce','tr','tl']):
        return 9
    elif all(x in strnum for x in['to','bo','br','bl','ce','tl']):
        return 6
    elif all(x in strnum for x in['to','bo','ce','br','tr']):
        return 3
    elif all(x in strnum for x in['to','bo','ce','br','tl']):
        return 5
    elif all(x in strnum for x in['to','bo','ce','tr','bl']):
        return 2
    elif strnum == "":
        return 0
    
def findsum(nums,numsOutput):
    dict={}
    lens = sorted(nums, key=len)
    dict.update({check(lens[1],lens[0]):"to"})
    for i in lens[-2:-5:-1]:
        if check(lens[-1],i) in lens[0]:
            dict.update({check(lens[-1],i):"tr"})
            dict.update({check(lens[0],check(lens[-1],i)):"br"})
            i6 = i
        elif check(lens[-1],i) not in lens[2]:
            dict.update({check(check(i,lens[2]),key("to",dict)):"bo"})
            dict.update({check(lens[-1],i):"bl"})
            i9 = lens.index(i)
        else:
            dict.update({check(lens[-1],i):"ce"})
            i0 = i
    for j in lens[-5:-8:-1]:
        if check(lens[i9],j) in lens[2] and check(lens[i9],j) not in lens[0]:
            dict.update({check(lens[i9],j):"tl"})
            i3 = j
    for i in range(len(numsOutput)):
        strnum = ""
        if len(numsOutput[i])==2:
            numsOutput[i]=1
        elif len(numsOutput[i])==3:
            numsOutput[i]=7
        elif len(numsOutput[i])==4:
            numsOutput[i]=4
        elif len(numsOutput[i])==7:
            numsOutput[i]=8
        else:
            for j in range(len(numsOutput[i])):
                strnum += dict[numsOutput[i][j]]
            numsOutput[i]=findnum(strnum)
    num = ""
    for i in numsOutput:
        num += str(i)
    num = int(num)
    return num
Sum = 0
for i in range(len(lis)):
    Sum += findsum(lis[i],lisOutput[i])
print(Sum)
