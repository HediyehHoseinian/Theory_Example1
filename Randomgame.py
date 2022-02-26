from pickle import TRUE
import random
computer_number=random.randint(0,100)
counter_guess=1
while True:
    
    user_number=int(input())

    if(computer_number== user_number):
            print("veryyyy Goooood! You Are Win")
            print("Count Of your guess:")
            print(counter_guess)
    elif (user_number>computer_number):
            print("Bia Paein")
            counter_guess +=1
    elif (user_number<computer_number):
            print("Boro Bala")
            counter_guess +=1
   
