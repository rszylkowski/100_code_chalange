# Calculator


import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
 }

print(art.logo)


def calculator():
    num1 = float(input("What's the first number?: "))

    for e in operations.keys():
        print(e)

    while True:
        operator = input("Pick an operation from the list above: ")
        while operator not in operations.keys():
            operator = input("Pick an operation from the list above: ")
        num2 = float(input("What's the next number?: "))
        function = operations[operator]
        answer = function(num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")
        num1 = answer
        continue_flag = input(
            f"Type 'y' to continue calculating with {answer},\ntype 'n' to begin new calculation,\
            \nor type 'q' to quit.: ")
        while continue_flag in ['ynq']:
            continue_flag = input(
                f"Type 'y' to continue calculating with {answer},\ntype 'n' to finis this calculation")
        if continue_flag == 'n':
            break


exit_flag = True
while exit_flag:
    calculator()
    if input(f"Type 'y' to start new calculation,\nor type 'q' to quit.: ") == 'q':
        break
