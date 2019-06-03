#!/usr/bin/python

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
        #if y<500-width-vol:
        #    y=y+vol
    #while x<500-width-vol:    

    #without trace
    screen.fill((0,0,0))          
    
    pygame.draw.rect(screen, (255,0,0), [x, y, width, height])
    pygame.display.update()
  #clock.tick(60)