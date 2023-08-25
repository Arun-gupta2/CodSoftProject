def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def divide(n1,n2):
    return n1/n2
def multiply(n1,n2):
    return n1*n2
operation={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    num1=float(input("enter first number"))
    for symbol in operation:
        print(symbol)
        should_continue=True
    while should_continue==True:
        operation_symbol=input("pick an operation:")
        num2=float(input("enter next number"))
        calculation_function=operation[operation_symbol]
        answer=calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2}={answer}")
        next_operation_choice=input("do you want to continue the calculation?type 'y' for yes and 'n' to start  new calculation and press x to exit")
        if next_operation_choice=='y':
            should_continue=True
            num1=answer
        elif next_operation_choice=='n':
            should_continue=False
            calculator()
        else:
            should_continue=False
            print("calculation ended!")
calculator()
        