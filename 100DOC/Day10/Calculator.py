#calculator
import art
print(art.logo)

#addition
def add(n1, n2):
    return n1 + n2
#subtraction
def subtract(n1, n2):
    return n1 - n2
#multiplication
def multiply(n1, n2):
    return n1 * n2
#division
def divide(n1, n2):
    return n1/n2

operations ={
    '+' : add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}
def calculator():
    num1 = float(input('Enter first number'))
    keep_goin = True
    while keep_goin == True:

        num2 = float(input('Enter second number'))

        for symbol in operations:
            print(symbol)
        operation_symbol = input('Pick an operation symbol from the line above: ')
        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)
        print(f'{num1}{operation_symbol}{num2} = {answer}')
        to_continue = input('do you want to keep going? Type Y to continue or N to stop')

        if to_continue == 'y':
            num1 = answer
        else:
            keep_goin = False
            calculator()
calculator()




