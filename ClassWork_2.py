#!/usr/bin/python
#-------------while_and_for----------
def bigger_or_smaller():
    print('Using while')
    a=98
    while a > 0:
        a=a-2
        print(a)

    print('Using for')

    for a in range(99):
        if (a%2):
            print(a+1)
    return

#-------w-continue_and_w/o----------
def continue_and_not():
    print('Using continue')
    a=100
    while a > 0:
        a=a-1
        if (a%2)==0:
            continue
        print(a)

    print('Not Using continue')
    a=100
    while a > 1:
        a=a-1
        print(a)    
    
    return

def odd_list():    
    list = (1,2,3,4,5,6)
    for a in list:
        if a%2 != 0:
            print(list)
            print("Exiting, the list has odd numbers")
            break
    else: 
        print("The list doesn't contain odd numbers")

print("Please choose function to run")
print("Available functions:")
print("    (1) while_and_for")
print("    (2) continue_and_not")
print("    (3) check list for odd numbers")
func_name=input()
if func_name==1:
    bigger_or_smaller()
elif func_name==2:
    continue_and_not()
elif func_name==3:
    odd_list()
else: print('invalid output')
