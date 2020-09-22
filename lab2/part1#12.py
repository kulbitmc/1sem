import turtle as t
import numpy as np
n = int(input())
def circle1():
    for i in range(180):
        t.right(1)
        t.forward(2*0.5*np.sin(0.5))
def circle2():
    for k in range(180):
        t.right(1)
        t.forward(2*0.05*np.sin(0.5))
for l in range(n):
    circle1()
    circle2()
