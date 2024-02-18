def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def prime_sums(x, prime):
    nums = []
    for i in range(0, len(prime)):
        for j in range(0, len(prime)):
            if prime[i] + prime[j] == x:
                nums.append(prime[i])
                nums.append(prime[j])
                return nums


prime = [ 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

file = open("pary.txt", "r")
numbers = []
for line in file:
    temp = line.split(" ")
    numbers.append(int(temp[0]))
file.close()
result = []
for x in numbers:
    if is_even(x):
        tmp=prime_sums(x,prime)
        result.append(str(x)+" "+str(tmp[0])+" "+str(tmp[1]))

for x in result:
    print(x)
