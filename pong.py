import sys
import pygame
from pygame.locals import *
import time

pygame.init()
# Resolution is ignored on Android
surface = pygame.display.set_mode((450,750))

score= 0
myfont = pygame.font.SysFont("Monospace", 64)
label = myfont.render(f'{score}', 1, (255, 255, 255))
clock = pygame.time.Clock()

#Colores
red= (255,0,0)
green= (0,255,0)
blue= (0,0,255)

#Bola
posX, posY= 200,350
velX, velY= 3,3

#Player1
playerX, playerY= 10, 300

#Player2
player2X, player2Y= 450, 300

while True:
    pygame.display.flip()
    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
    # Framelimiter
    
    posX += velX
    posY += velY
    
    if posX> 450 or posX<0:
       posX= 200
       posY= 350
       score += 1
       time.sleep(1)
       velX *= -1
       
    if posY > 750 or posY <0:
       velY *= -1
       
    pos= pygame.mouse.get_pos()
    playerY= pos[1]
    player2Y= pos[1]
       
    surface.fill((0, 0, 0))
    surface.blit(label, (220,10))
    
    bola= pygame.draw.rect(surface, green, (posX, posY, 50,50))
    
    player1= pygame.draw.rect(surface, blue, (playerX, playerY, 10,200))
    
    player2= pygame.draw.rect(surface, blue, (player2X, player2Y, 10,200))
    
    if bola.colliderect(player1) or bola.colliderect(player2):
    	velX *= -1
    	
    score += 1
    clock.tick(60)
