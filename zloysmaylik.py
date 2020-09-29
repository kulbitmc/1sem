import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill ((211, 211, 211))

circle (screen, (255, 255, 0), (200, 200), 100)
circle (screen, (0, 0, 0), (200, 200), 100, 1)

rect (screen, (0, 0, 0), (150, 240, 100, 20))

circle (screen, (255, 0, 0), (150, 180), 20)
circle (screen, (0, 0, 0), (150, 180), 20, 1)
circle (screen, (0, 0, 0), (150, 180), 8)

circle (screen, (255, 0, 0), (250, 180), 15)
circle (screen, (0, 0, 0), (250, 180), 15, 1)
circle (screen, (0, 0, 0), (250, 180), 8)


polygon (screen, (0, 0, 0), [(110, 125), (170, 170), (179, 158), (119, 113)])
line (screen, (0, 0, 0),(230, 164), (290,140), 15)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
