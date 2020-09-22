import turtle as t
import numpy as np
t.shape('classic')
t.speed(11)
def circle(d):
    t.goto(0,0)
    for i in range(360): 
        t.forward(d)
        t.right(1)
        t.forward(2*d*np.sin(0.5))
n = int(input())
for i in range(n):
    circle(0.05 + i * 0.05)
    t.right(180)
    circle(0.05 + i * 0.05)
    t.left(180)
