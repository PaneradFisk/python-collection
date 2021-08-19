valueErrorMsg = "!!! NOT A NUMBER, RESTARTING SESSION. !!!"
numErrorMsg = "That's not a number, try again."
choiceErrorMsg = "Choice not avaiable, try again."

def calculator(math_operator):
    print("*" * 30)
    try:
        num1 = int(input("Please enter first number: "))
    except ValueError:
        print(valueErrorMsg)
        calculator(math_operator)
    try:
        num2 = int(input("Enter second number: "))
    except ValueError:
        print(valueErrorMsg)
        calculator(math_operator)
    if math_operator == "1":
        print("Sum:", num1 + num2)
    elif math_operator == "2":
        print("Difference:", num1 - num2)
    elif math_operator == "3":
        print("Product:", num1 * num2)
    elif math_operator == "4":
        print("Quotient:", num1 / num2)
    elif math_operator == "5":
        print("Remainder:", num1 % num2)
    else:
        print("??? how did we end up here?")
    print("*" * 30)

while True:
    strX = input("""
    Available choices;
    exit - Quit program
    1 - Addition
    2 - Subtraction
    3 - Multiplication
    4 - Division
    5 - Modulo
    Please enter a number: """)
    # try:
    #     numX = int(strX)
    # except:
    #     print(numErrorMsg)
    #     continue
    
    if strX == "exit":
        quit()
    elif strX == "1" or "2" or "3" or "4" or "5":
        calculator(strX)
    else:
        print(choiceErrorMsg)
        continue

    # if strX == "1" or "2" or "3" or "4" or "5":
    #     calculator(strX)
    # elif strX == "exit":
    #     quit()
    # else:
    #     print(choiceErrorMsg)
    #     continue
