#!/usr/bin/python
#-------------bigger or smaller----------
def bigger_or_smaller():
    a = input("Please enter a for comparison \n")
    print("a=")
    b = input("Please enter b for comparison \n")
    print("b=")
    if a>b:
        print('a>b')
    else: print('b>a')
    return

#-------odd or not----------
def odd_or_not():
    a = input("Please enter a for odd determination \n")
    if (a%2):
        print('is odd')
    else:
        print('is not odd')
    a = input()

def factorial_internal(n):    
    if n == 0:
        return 1
    return factorial_internal(n-1) * n

def factorial_external():
    
    factorial_internal(n)
    return n

print("Please choose function to run")
print("Available functions:")
print("    (1) bigger_or_smaller")
print("    (2) odd_or_not")
print("    (3) factorial")
func_name=input()
if func_name==1:
    bigger_or_smaller()
elif func_name==2:
    odd_or_not()
elif func_name==3:
    n = input("Please enter value for factorial calculation")
    print(factorial_internal(n))
else: print('invalid output')
