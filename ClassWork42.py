#!/usr/bin/python
#pylint: disable=C0321 
import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


pygame.init()
 

screen = pygame.display.set_mode([800, 600])
 

pygame.display.set_caption('Fly')
 
clock = pygame.time.Clock()


pygame.display.update()
 

background_position = [0, 0]
 

player_image = pygame.image.load("/Users/msulym/Documents/Repository/truexenom-first/1.png").convert()


player_image.set_colorkey(BLACK)
 
done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True            
 
    

    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
 

    screen.blit(player_image, [x, y])
 

    pygame.display.flip()
 
    clock.tick(60)


pygame.quit()