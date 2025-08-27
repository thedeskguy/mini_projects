from art import logo
print(logo)
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
operation={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}
# print(operation["*"](2,2))
def calc():
    num1=int(input("Give me the first number:\n"))
    ans=0
    while True:
        for symbol in operation:
            print(symbol)
        op=input("what operatioon do you wanna perform:\n")
        num2=int(input("Give me your second number: \n"))
        if op=="+":
            ans=operation["+"](num1,num2)
        elif op=="-":
            ans=operation["-"](num1,num2)
        elif op=="*":
            ans=operation["*"](num1,num2)
        elif op=="/":
            ans=operation["/"](num1,num2)
        print(f"Your value is: {num1} {op} {num2} = {ans}")
        con=input(f"If you wanna continue operations on {ans} type 'y' else type 'n' \n")
        if con=="n":
            break
        else:
            num1=ans
calc()