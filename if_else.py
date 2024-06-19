'''number = int(input("Enter a number: "))
if number >= 0:
    print("The number is Positive")
else:
    print("The number is Negative")'''
    
'''number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")'''

'''cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

if cost_price > selling_price:
    loss = cost_price - selling_price
    print("Incurred loss ", loss)
elif cost_price < selling_price:
    profit = selling_price - cost_price
    print("Profit ",profit)
else:
    print("No profit or No loss")'''


'''marks = float(input("Enter percentage of a student: "))
if 81 < marks <= 100:
    print("Very Good")

elif 61 < marks < 80:
    print("Good")

elif 41 < marks < 60:
    print("Average")

else:
    print("Fail")'''

'''eng_marks = float(input("Enter marks in english "))
maths_marks = float(input("Enter marks in maths "))

if eng_marks > 80 and maths_marks > 80:
    print("Grade - A ")

elif eng_marks < 80 and maths_marks > 80:
    print("Grade - B ")

elif eng_marks > 80 and maths_marks < 80:
    print("Grade - B ")

else:
    print("Grade - C ")'''


'''number = int(input("Please enter your number "))

if number >= 1000 and number <= 9999:
    print("This is four digit number")
else:
    print("This is not four digit number")'''



'''n1 = float(input(" Input first number "))
n2 = float(input("Input second number "))
n3 = float(input(" Input third number "))

if n3 > n2 and n3 > n1:
    print(n3, "The third number is greatest")

elif n2 > n1 and n2 > n3:
    print(n2, "The second number is greatest")

elif n1 > n2 and n1 > n3:
    print(n1, "The first number is greatest")'''


#using nested if  else statement

'''n1 = float(input(" Input first number "))
n2 = float(input("Input second number "))
n3 = float(input(" Input third number "))

if n1 > n2:
    #either n1 or n3 is greatest
    if n1 > n3:
        print(n1, " is the greatest element")
    else:
        print(n3, " is the greatest element")
else:
    #either n2 or n3 is greatest
    if n2 > n3:
        print(n2, " is the greatest element")
    else:
        print(n3, " is the greatest element")'''


n = int(input("Enter a number "))

#checking whether it is divisible by 15
if n % 15 == 0:
    print("this is divisible by 15.")
else:
    #checking if divisible by 3 or 5
    if n % 5 == 0 or n % 3 == 0:
        print("this is divisible by 5 or 3 but not divisible by 15.")
    else:
        print("this number is neither divisible by 3 nor by 5.")





