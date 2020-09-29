import pygame
import numpy
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 800 ))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BEIGE = (210, 180, 140)
SADDLEBROWN = (139, 69, 19)
SKYBLUE = (135, 206, 235)
SEABLUE = (70, 0, 205)
CHOCOLATE = (210, 105, 30)
CRIMSON = (220, 20, 60)


rect (screen, SKYBLUE, (0, 0, 1000, 400))
rect (screen, SEABLUE , (0, 400, 1000, 180))
rect (screen, YELLOW, (0, 580, 1000, 220))


circle (screen, YELLOW, (850, 150), 75)


arc(screen, SADDLEBROWN, (550, 380, 100, 100), numpy.pi, 1.5*numpy.pi, 200)

rect (screen, SADDLEBROWN, (600, 430, 250, 50))
line (screen, BLACK,(600, 430), (600, 480))

line (screen, BLACK, (650, 430), (650, 280), 10)
polygon (screen, BEIGE, [(655,430),(680, 355), (655, 280), (760, 355)])
polygon (screen, BLACK, [(655,430),(680, 355), (655, 280), (760, 355)], 1)
line (screen, BLACK, (680, 355), (760, 355))

polygon (screen, SADDLEBROWN, [(850, 430),(850, 480), (970, 430)])
line (screen, BLACK, (850, 430), (850, 480))
circle (screen, BLACK, (875, 450), 16)
circle (screen, WHITE, (875, 450), 10)


rect (screen, CHOCOLATE, (150, 780, 10, -240))
rect (screen, CRIMSON, (150, 540, 10, -50))
polygon (screen, CRIMSON, [(150, 490),(160, 490),(260, 540),(50, 540)])
rect (screen, BLUE, (150, 540, 10, -50), 1)
line (screen, BLACK, (80, 540), (150, 490))
line (screen, BLACK, (110, 540), (150, 490))
line (screen, BLACK, (140, 540), (150, 490))
line (screen, BLACK, (230, 540), (160, 490))
line (screen, BLACK, (200, 540), (160, 490))
line (screen, BLACK, (170, 540), (160, 490))


circle (screen, WHITE, (220, 100), 30)
circle (screen, BLACK, (220, 100), 30, 1)

circle (screen, WHITE, (260, 100), 30)
circle (screen, BLACK, (260, 100), 30, 1)

circle (screen, WHITE, (200, 130), 30)
circle (screen, BLACK, (200, 130), 30, 1)

circle (screen, WHITE, (235, 133), 30)
circle (screen, BLACK, (235, 133), 30, 1)

circle (screen, WHITE, (270, 136), 30)
circle (screen, BLACK, (270, 136), 30, 1)

circle (screen, WHITE, (300, 100), 30)
circle (screen, BLACK, (300, 100), 30, 1)

circle (screen, WHITE, (305, 139), 30)
circle (screen, BLACK, (305, 139), 30, 1)




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()