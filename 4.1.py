def is_even(x):
    if x % 2==0:
        return True
    else:
        return False


file=open("przyklad.txt","r")
numbers=[]
for line in file:
    temp=line.split(" ")
    numbers.append(int(temp[0]))
file.close()
for x in numbers:
    if is_even(x):
        print(x)