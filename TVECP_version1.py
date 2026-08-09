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

def exponentialtion(n1,n2):
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
    if operator == "+":
        result = addition(number_1,number_2)
        print(f"The result of {number_1} + {number_2} is {result}")
    elif operator == "-":
        result = subtraction(number_1,number_2)
        print(f"The result of {number_1} - {number_2} is {result}")
    elif operator == "*":
        result = multiplication(number_1,number_2)
        print(f"The result of {number_1} * {number_2} is {result}")
    elif operator == "/":
        result = division(number_1,number_2)
        print(f"The result of {number_1} / {number_2} is {result}")
    elif operator == "//":
        result = floordivision(number_1,number_2)
        print(f"The result of {number_1} // {number_2} is {result}")
    elif operator == "**":
        result = exponentialtion(number_1,number_2)
        print(f"The result of {number_1} ** {number_2} is {result}")
    elif operator == "%":
        result = modulo(number_1,number_2)
        print(f"The result of {number_1} % {number_2} is {result}")
    else:
        print("Please Select Operator.")

number_1,number_2 = enter_number()
operator = enter_operator()
main_operator(number_1,number_2,operator)

