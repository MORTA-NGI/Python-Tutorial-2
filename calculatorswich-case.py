def sum(number1, number2):
    sum =number2+number1
    return sum   

def divition(number1, number2):
    div =number2/number1
    return div
def mult(number1, number2):
    mult =number2*number1
    return mult   

def sub(number1, number2):
    sub =number1-number2
    return sub
while True:
    no1=int(input("Enter the number 1: "))
    no2=int(input("Enter the number 2: "))
    sign=input("Enter the operation (+,-,*, or /): ")
    

    match sign:
        case '+':
            result=sum(no1, no2)
            print('result of sum is ' , result)
        case '-':
            result=sub(no1, no2)
            print('result of sub is ' , result)
        case '/':
            result=divition(no1, no2)
            print('result of div is ' , result)
        case '*':
            result=mult(no1, no2)
            print('result of multi is ' , result)