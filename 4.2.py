file=open("pary.txt","r")
text=[]
for line in file:
    temp=line.split(" ")
    text.append(temp[1].rstrip())

result=[]

for x in text:
    longest=x[0]
    counter=1
    currentFramgent=""
    currentCounter=1
    for i in range(0,len(x)-1):
        if x[i]==x[i+1]:
            currentCounter+=1
            currentFramgent+=x[i]
            if currentCounter > counter:
                longest=currentFramgent
                counter=currentCounter
        else:
             currentFramgent=""
             currentCounter=1
    result.append(longest+" "+str(counter))

for x in result:
    print(x)

