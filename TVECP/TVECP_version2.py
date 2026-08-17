def addition(n1,n2):
    result = n1+n2
    return result

def subtraction(n1,n2):
    result = n1-n2
    return result

def multiplication(n1,n2):
    result = n1*n2
    return result

def division(n1,n2):
    result = n1/n2
    return result

def floordivision(n1,n2):
    result = n1//n2
    return result

def exponentiation(n1,n2):
    result = n1**n2
    return result

def modulo(n1,n2):
    result = n1%n2
    return result

def enter_number():
    number_1 = float(input("Enter the first number : "))
    number_2 = float(input("Enter the second number : "))
    return number_1,number_2

def enter_operator():
    operator = input("Enter the Operator : ")
    return operator

def main_operator(number_1,number_2,operator):
    match operator:
        case "+":
            result = addition(number_1,number_2)
            print(f"The result of {number_1} + {number_2} is {result}")
        case "-":
            result = subtraction(number_1,number_2)
            print(f"The result of {number_1} - {number_2} is {result}")
        case "*":
            result = multiplication(number_1,number_2)
            print(f"The result of {number_1} * {number_2} is {result}")           
        case "/":
            result = division(number_1,number_2)
            print(f"The result of {number_1} / {number_2} is {result}")
        case "//":
            result = floordivision(number_1,number_2)
            print(f"The result of {number_1} // {number_2} is {result}")
        case "**":
            result = exponentiation(number_1,number_2)
            print(f"The result of {number_1} ** {number_2} is {result}")
        case "%":
            result = modulo(number_1,number_2)
            print(f"The result of {number_1} % {number_2} is {result}")
        case _:
            print("Please Select Operator.")

number_1,number_2 = enter_number()
operator = enter_operator()
main_operator(number_1,number_2,operator)

