#!/usr/bin/python

#------------------
#1-----

# number=int(input("Please enter the number\n"))
# try:
#     if number<=0:
#         raise ValueError
#     if number%2==0:
#         print("Number is Even")
#     if number%2<>0:
#         print("Number is Odd")
# except NameError:
#     print("Huston we have a problem\n")
# except ZeroDivisionError:
#     print("ZeroDivisionError message\n")
# except SyntaxError:
#     print("SyntaxError message\n")
# except TypeError:
#     print("TypeError message\n")
# except ValueError:
#     print("You Can't use value that is less than or equal to 0\n")

# finally:
#     print("Program Finished")


#-------------
#2---

# Class CustomError(Exception):
#     def __init__(self,data):
#         self.data = data
#     def __str__(self):
#         return repr(self.data)


# def age():
#     try:
#         number=int(input("Please enter your age\n"))
#         if number<=0:
#             raise ValueError
#         if number%2==0:
#             print("Your age is Even")
#         if number%2<>0:
#             print("Your age is Odd")
#     except NameError:
#         print("Huston we have a problem\n")
#     except ZeroDivisionError:
#         print("ZeroDivisionError message\n")
#     except SyntaxError:
#         print("SyntaxError message\n")
#     except TypeError:
#         print("TypeError message\n")
#     except ValueError:
#         print("You Can't use value that is less than or equal to 0\n")

#     finally:
#         print("Program Finished. Good Bye and  take care")

# age()

#----------------------
#3---

try:
    number1,number2=input("Please enter your numbers. Please use \"comma\" as separator\n")
    # if numbers<=0:
    #     raise ValueError

    print("The result of deviding two values are", number1/number2 )
    
    
except NameError:
    print("Huston we have a NameError problem\n")
except ZeroDivisionError:
    print("ZeroDivisionError message\n")
except SyntaxError:
    print("SyntaxError message\n")
except TypeError:
    print("TypeError message\n")
except ValueError:
    print("ValueError message\n")

finally:
    print("Program Finished. Good Bye and  take care")


#---------------------
#4---

# try:
#     number=int(input("Please enter day of week\n"))
#     if number<=0:
#         raise ValueError
#     if number==1:
#         print("The Day of week is Monday")
#     if number==2:
#         print("The Day of week is Tuesday")
#     if number==3:
#         print("The Day of week is Wednesday")   
#     if number==4:
#         print("The Day of week is Thursday")
#     if number==5:
#         print("The Day of week is Friday")
#     if number==6:
#         print("The Day of week is Saturday")
#     if number==7:
#         print("The Day of week is Sunday")
#     if number>=8:
#         raise ValueError

# except NameError:
#     print("You have entered a string instead of integer\n")
# except ZeroDivisionError:
#     print("ZeroDivisionError message\n")
# except SyntaxError:
#     print("SyntaxError message\n")
# except TypeError:
#     print("TypeError message\n")
# except ValueError:
#     print("You Can't use value that is less than, equal to 0 or bigger than 7\n")

# finally:
#     print("Program Finished. Good Bye and  take care")