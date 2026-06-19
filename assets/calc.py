import os   

def sum(num1, num2): 
    result = num1 + num2
    return result


def subtract(num1, num2): 
    result = num1 - num2
    return result


def multiply(num1, num2): 
    result = num1 * num2
    return result


def divide(num1, num2): 
    result = num1 / num2
    return result


def pow(num1, num2):
    result = num1
    for i in range(2, num2+1):
        result = result*i
    return result


def print_result(num1, num2, operation, result):
    print("{0} {1} {2} = {3}".format(num1, operation, 
                                     num2, result))
    input("Press enter to continue")


def print_menu(): 
    os.system('clear')
    print("Operations available -\n"
          "1. Add\n"
          "2. Subtract\n"
          "3. Multiply\n"
          "4. Divide\n"
          "5. Power\n"
          "6. Exit")

def call_calculator(number_1, number_2, option):
    number_1 = int(number_1)
    number_2 = int(number_2)

    if option == 1:
        operation = '+'
        result = sum(number_1, number_2)
    elif option == 2:
        operation = '-'
        result = subtract(number_1, number_2)
    elif option == 3:
        operation = 'x'
        result = multiply(number_1, number_2)
    elif option == 4:
        operation = '/'
        result = divide(number_1, number_2)
    elif option == 5:
        operation = '^'
        result = pow(number_1, number_2)
    print_result(number_1, number_2, operation, result)



while True: 
    print_menu()
    option = int(input("Select an option:"))
    if (option == 6): 
        break;

    number_1 = input("Enter first number: ") 
    number_2 = input("Enter second number: ")

    call_calculator(number_1, number_2, option)


