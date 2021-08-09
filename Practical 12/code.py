def simple_calculator(number1, number2, operator_string):
    if str(operator_string) == "+":
        return float(number1)+float(number2)
    elif str(operator_string) == "-":
        return float(number1)-float(number2)
    elif str(operator_string) == "*":
        return float(number1)*float(number2)
    elif str(operator_string) == "/":
        return float(number1)/float(number2)
    else:
        return "Invalid operator input..."


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the first number: "))
operator = str(input("Enter the operator: "))
print("The desired result is: ", simple_calculator(num1, num2, operator))

