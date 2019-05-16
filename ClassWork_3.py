#!/usr/bin/python
#-----------------1--min,max

def min_and_max():
    list=input("Please input the list \n")
    print("You have entered this list")
    print(list)
    print(min(list))
    print(max(list))

#-----------------2--

def list_devidables():
    list=[1,2,3,4,5,6,7,8,9,10]
    print("Our list is")
    print(list)
    print("Determining all numbers that are devidable by 2")
    for x in list:
        if (x%2==0):
            print(x)
    print("Determining not odd numbers devidable by 3")
    for x in list:
        if (x%2):
            if (x%3==0):
                print(x)
    print("Determining numbers that are not devidable by 2 or 3")
    for x in list:
        if not (x%2==0):
            if not (x%3==0):
                print(x)

#-------------------3--factorial-without-recursion

def factorial_without_recursion():
    number = int(input("Please enter number to calculate factorial \n")) 
    counter = 1
    if number <0:
        print("Factorial does not exist for negative numbers")
    else:
        while number > 1:
            counter *= number
            number -= 1
        print(counter)

#-----------------4--login

def login_check():
    login=raw_input("Please enter login \n")
    counter=0
    while counter < 1:
        counter=+1
        if login in ['First']:
            print("Your login is correct \n")
        else:
            print("Your login is not correct \n")

#-----------------5

def while_true():
    while True:
        number=input("Please enter the number \n")
        if number<0:
           break

#-----------------6



print("Please choose function to run")
print("Available functions:")
print("    (1) min_and_max")
print("    (2) list_devidables")
print("    (3) check list for odd numbers")
print("    (4) login_check")

func_name=input()
if func_name==1:
    min_and_max()
elif func_name==2:
    list_devidables()
elif func_name==3:
    factorial_without_recursion()
elif func_name==4:
    login_check()
elif func_name==5:
    while_true()

else: print('invalid output')
