#---------більше чи менше

a = input()
b = input()
if a>b:
    print('a>b')
else:
    print('b>a')

#-------Парне чи не парне

a = input()
if (a%2):
    print('is not parne')
else: 
    print('is parne')
a = input()


#-------Факторіал
def factorial(a):
    if a ==0:
        return 1
    return factorial(a-1) * a

print (factorial(a))

