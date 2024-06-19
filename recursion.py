#Q. find factorial till n.
'''def factorial(n):
    if n == 0:
        return 1
    ans = n * factorial(n -1)
    return ans

n = int(input("Enter n: "))
print(factorial(n))
'''
#Q. write a program to print n to 1.
'''def print_n_to_1(n):
    #base case
    if n == 0:
        return
    print(n)
    #recursive case
    print_n_to_1(n-1)
    
n = int(input("Enter n: "))
print_n_to_1(n)'''

#Q. write a program to print sum from 1 to n.

'''def sum_1_to_n(n):
    if n == 0:
        return 0
    ans = n + sum_1_to_n(n-1)
    return ans

n = 6
print(sum_1_to_n(n))
'''

#Q. make a function which calculates "a" raised to the power "b" using recusion.

'''def power_a_b(a,b):
    #base case
    if b == 0:
        return 1
    
    #recursive case
    ans = a * power_a_b(a,b-1)
    return ans

a = 4
b = 3
print(power_a_b(a,b))
    '''

#Q. make a function which calculates fibonacci sequence using resucion.
def fibonacci(n):
    
    if n == 1:           #base case
        return 0
    elif n == 2:         #base case
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))        #resursive case
    
n = int(input("Enter n: "))
for i in range(1,n+1):
    print(fibonacci(i))








