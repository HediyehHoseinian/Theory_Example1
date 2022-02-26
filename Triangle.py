number1 = int(input("pls Enter number 1 : "))
number2 = int(input("pls Enter number 2 : "))
number3 = int(input("pls Enter number 3: "))

if number1< number2+number3 and number2<number1+number3 and number3<number1+number2:
    print("this is a triangle")
else:
    print("it is not a triangle")