def sum(number1, number2):
    sum =number2+number1
    return sum   

def divition(number1, number2):
    div =number2/number1
    return div
def mult(number1, number2):
    mult =number2+number1
    return mult   

def sub(number1, number2):
    sub =number1-number1
    return sub

no1=int(input("Enter the number 1: "))
no2=int(input("Enter the number 2: "))
if no1> 0:
    result=divition(no1, no2)
    print('result2 ' , result)
else:
    result=sum(no1, no2) 
    print('result ' ,result)
