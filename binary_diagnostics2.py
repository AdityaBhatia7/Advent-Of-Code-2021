with open("C:/Users/Aditya/OneDrive/Desktop/Advent Of Code/day3.txt") as m:
    lines = m.read().splitlines()
linescopy_o2 = lines
linescopy_co2 = lines
o2_rate = ""
co2_rate = ""
element_len = len(lines[0])
def nlist_o2(x, index):
    count0 = 0
    count1 = 0
    nlines_o2 = []
    i = index
    for j in range(len(x)):
        if x[j][i]=="0":
            count0 += 1
        else:
            count1 += 1
    if count0 > count1:
        for l in range(len(x)):
            if x[l][i]=="0":
                nlines_o2.append(x[l])
    elif count1 > count0:
        for m in range(len(x)):
            if x[m][i]=="1":
                nlines_o2.append(x[m])
    elif count1 == count0:
        for n in range(len(x)):
            if x[n][i]=="1":
                nlines_o2.append(x[n])
    return nlines_o2
def nlist_co2(y, index):
    count0 = 0
    count1 = 0
    nlines_co2 = []
    i = index
    for k in range(len(y)):
        if y[k][i]=="0":
            count0 += 1
        else:
            count1 += 1
    if count0 < count1:
        for l in range(len(y)):
            if y[l][i]=="0":
                nlines_co2.append(y[l])
    elif count1 < count0:
        for m in range(len(y)):
            if y[m][i]=="1":
                nlines_co2.append(y[m])
    elif count1 == count0:
        for n in range(len(y)):
            if y[n][i]=="0":
                nlines_co2.append(y[n])
    return nlines_co2
for i in range(element_len):
    linescopy_o2 = nlist_o2(linescopy_o2,i)
for k in range(element_len):
    linescopy_co2 = nlist_co2(linescopy_co2,k)
    if len(linescopy_co2)==1:
        break
o2_rate = int(linescopy_o2[0],2)
co2_rate = int(linescopy_co2[0],2)
print(o2_rate*co2_rate)
