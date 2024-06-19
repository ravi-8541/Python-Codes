'''n = int(input("enter n: "))

for _ in range(n):
    print("1" *)
'''

'''n = int(input("enter n: "))

for i in range(n): #loop for rows
    for j in range(1, n + 1):  #loop for columns
        print(j, end="")
    print()
'''


'''n = int(input("enter n: "))

for i in range(1, n+1):    #loop for rows
    for j in range(1, i+1):  #loop for columns
        print(j, end="")
    print()
'''

n = int(input("Enter n: "))

for i in range(1, n+1): #loop for rows
    #printing space
    print(" " * (n-i), end="")

    #printing digits
    for j in range(1, 2 * i):
        print(j, end="")
    print()


