'''n = int(input("Enter N: "))

sum = 0
for i in range(1,n+1):
    sum += i

print("sum of all the numbers till `N` is: ",sum)

sum1 = 0
for i in range(1,n+1):
    sum1 += i

print("sum of all the numbers till `N` is: ",sum)'''

#writing a function for calculating sum form 1 to N

def sumTillN(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

#call function
n = int(input("Enter N: "))
output = sumTillN(n)
print("The value is: ",output)