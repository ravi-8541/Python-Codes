#write a function that prints hello world
'''
def printHello():
    #body of function
    print("Helloworld!!")

printHello()'''

#Functions which takes two numbers as input and returns their sum.
#yaha maine ravi name se ek function banaya jiska kaam h two variables ko add karna.

#jahan jahan ravi type karenge as a function ye add karega 
'''def ravi(n1,n2=6):
    
    sum = n1 + n2
    return sum

print("The sum is ",ravi(3))'''

'''def addAllNumbers(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

output = addAllNumbers(9,10,2,5,17,66)

print("The sum is",output)
'''

def studentInfo(**kwargs):
    for x,y in kwargs.items():
        print(x,"is",y)

studentInfo(name="ravi", age=23, city="patna")
studentInfo(name="reshmi", age=22, city="patna")
studentInfo(name="ishika", age=7, city="patna")


