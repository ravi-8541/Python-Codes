num1 = float(input("Enter number 1: "))
operator = input(  "Enter operator: ")
num2 = float(input("Enter number 2: "))

match operator:
    case "+":
        print("sum is ", num1 + num2)
    case "-":
        print("difference is ", num1 - num2)
    case "*":
        print("multiplication is ", num1 * num2)
    case "/":
        print("division is ", num1 / num2)
    case _ :
        print("Enter a valid operator.")

        