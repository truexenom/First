#!/usr/bin/python
#----------1-----------

def random_number():
    import random
    number =random.randint(1,100)
    print(number)

#----------2------

def number_game():
    while True:
        user_number=input("Please enter your number \n")
        if user_number == number:
            print("You ROCK! Correct number!")
            break
        elif user_number < number:
            print("Your number is smaller than should be")
        elif user_number > number:
            print("Your number is bigger that should be")

#------------3--------------

def calc
    import math
    a=input("Please enter a\n")
    b=input("Please enter b")
    h=input("Please enter h")
    r=input("please enter r")
    print("plos4a priamokutnuka= \n")
    print(a*b)
    print("plos4a trukutnuka= \n")
    print(0.5*h*a)
    print("plos4a kola= \n")
    print(pi*r**2)


print("Please choose function to run")
print("Available functions:")
print("    (1) random_number")
print("    (2) number_game")
print("    (3) calc")

func_name=input()
if func_name==1:
    random_number()
elif func_name==2:
    number_game()
elif func_name==3:
    calc()

else: print('invalid output')
