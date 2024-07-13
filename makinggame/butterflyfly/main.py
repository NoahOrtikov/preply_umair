# make a pygame in which butterfly picture will rotate and go up and down 

import pygame
import sys
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('butterfly game')

clock = pygame.time.Clock()

butterflyImg = pygame.image.load('/Users/noahjaceortikov/Desktop/preply/makinggame/butterflyfly/btf.png')

x = display_width * 0.45
y = display_height * 0.8
x_change = 0
y_change = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
            if event.key == pygame.K_UP:
                y_change = -5
            if event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0

    x += x_change
    y += y_change
    gameDisplay.fill(white)
    gameDisplay.blit(butterflyImg,(x,y))
    pygame.display.update()
    clock.tick(60)