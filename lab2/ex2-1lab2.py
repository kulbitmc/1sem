import turtle
turtle.shape('classic')
from random import *
n = randint (50, 100)
for i in range (n):
        turtle.forward (randint (0, 100))
        turtle.left (randint(0, 360))
