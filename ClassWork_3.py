#!/usr/bin/python
#-----------------1--min,max

# list=input("Please input the list \n")
# print("You have entered this list")
# print(list)
# print(min(list))
# print(max(list))

#-----------------2--

# list=[1,2,3,4,5,6,7,8,9,10]
# print("Our list is")
# print(list)
# print("Determining all numbers that are devidable by 2")
# for x in list:
#     if (x%2==0):
#         print(x)
# print("Determining not odd numbers devidable by 3")
# for x in list:
#     if (x%2):
#         if (x%3==0):
#             print(x)
# print("Determining numbers that are not devidable by 2 or 3")
# for x in list:
#     if not (x%2==0):
#         if not (x%3==0):
#             print(x)

#-------------------3--factorial-without-recursivness

# number = int(input("Please enter number to calculate factorial \n")) 
# counter = 1
# if number <0:
#     print("Factorial does not exist for negative numbers")
# else:
#     while number > 1:
#         counter *= number
#         number -= 1
#     print(counter)

#-----------------4--login

# login=raw_input("Please enter login \n")
# counter=0
# while counter < 1:
#     counter=+1
#     if login in ['First']:
#         print("Your login is correct \n")
#     else:
#         print("Your login is not correct \n")

#-----------------5

# while True:
#     number=input("Please enter the number \n")
#     if number<0:
#         break

#-----------------6
list=(1,2,3,4,5,6,7,8,9,0)
import pyowm
