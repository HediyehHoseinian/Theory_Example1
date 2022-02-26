from cmath import sin
import math


while True:

    operator=input()
    if operator=="exit":
        print("Bye Bye")
        break
    elif operator=="sin" or operator=="log" or operator=="fact" or operator=="tan" or operator=="sqrt":
        num1=float(input())
    else:
        num1 = float(input())
        num2 = float(input())

    if operator=="+":
        result = num1+num2

    elif operator == "-":
        result= num1-num2

    elif operator == "*":
        result=num1*num2

    elif operator=="**" or operator=="^":
        result= math.pow(num1,num2)

    elif operator=="sin":
        result=math.sin(num1)

    elif operator=="log":
        result=math.log(num1)

    elif operator=="fact":
        result=math.factorial(num1)
    
    elif operator=="tan":
        result=math.tan(num1)

    elif operator=="sqrt":
        result=math.sqrt(num1)

    elif operator=="/":
        if num2==0:
            print("cannot devide by zero")
        else:
            result=num1/num2



    print(result)