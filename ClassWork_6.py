#!/usr/bin/python
#----------1-----------

# def random_number():
#     import random
#     number =random.randint(1,100)
#     print(number)

# #----------2------

# def number_game():
#     while True:
#         user_number=input("Please enter your number \n")
#         if user_number == number:
#             print("You ROCK! Correct number!")
#             break
#         elif user_number < number:
#             print("Your number is smaller than should be")
#         elif user_number > number:
#             print("Your number is bigger that should be")

# #------------3--------------

# def calc
#     import math
#     a=input("Please enter a\n")
#     b=input("Please enter b")
#     h=input("Please enter h")
#     r=input("please enter r")
#     print("plos4a priamokutnuka= \n")
#     print(a*b)
#     print("plos4a trukutnuka= \n")
#     print(0.5*h*a)
#     print("plos4a kola= \n")
#     print(pi*r**2)


# print("Please choose function to run")
# print("Available functions:")
# print("    (1) random_number")
# print("    (2) number_game")
# print("    (3) calc")

# func_name=input()
# if func_name==1:
#     random_number()
# elif func_name==2:
#     number_game()
# elif func_name==3:
#     calc()

# else: print('invalid output')


import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("My first game")
#clock = pygame.time.Clock()

x=50
y=50
width=40
height=60
vol=5


run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x>vol:
        x=x-vol
    if keys[pygame.K_RIGHT] and x<500-width-vol:
        x=x+vol
    if keys[pygame.K_UP] and y>vol:
        y=y-vol
    if keys[pygame.K_DOWN] and y<500-width-vol:
        y=y+vol


    #without trace
    screen.fill((0,0,0))          
    
    pygame.draw.rect(screen, (255,0,0), [x, y, width, height])
    pygame.display.update()
  #clock.tick(60)