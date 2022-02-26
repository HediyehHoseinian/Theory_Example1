weight = float(input("please enter your weight : "))
heigh = float(input("please enter your heigh : "))

bmi = weight / (heigh*heigh)

if(bmi < 18.5):
    print("your BMI is", bmi,  "you have underwight")
elif(bmi < 24.9):
    print("your BMI is", bmi, " you are normal ")
elif(bmi < 29.9):
    print("your BMI is", bmi,  "you have owerweight")
elif(bmi < 34.9):
    print("your BMI is", bmi,  "you are obese")
else:
    print("your BMI is", bmi,  "you are extremeli obese")
