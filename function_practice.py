'''#function for calculating factorial

def factorial(n):
    ans = 1
    for i in range(1 , n+1):
        ans *= i
    return ans

#call function
n = int(input("Enter N: "))
output = factorial(n)
print("the factorial is: ",output)

'''

#practice MCQ.1

def say(message,times = 1):
    print(message * times)

say("hello")
say("world",5)



