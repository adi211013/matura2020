file=open("pary.txt","r")
pairs=[]
for line in file:
    line=line.rstrip()
    temp=line.split()
    if int(temp[0])==len(temp[1]):
        pairs.append(temp)
file.close()
l=pairs[0]
for i in range(1,len(pairs)):
    if int(pairs[i][0])<int(l[0]):
        l.clear()
        l=pairs[i]
    elif int(pairs[i][0])==int(l[0]) and pairs[i][1]<l[1]:
        l.clear()
        l=pairs[i]

print(l)