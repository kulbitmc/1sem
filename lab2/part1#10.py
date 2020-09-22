import turtle as t
import numpy as np
n = int(input())
def circle():
    for i in range(180):
        t.right(2)
        t.forward(2*0.5*np.sin(0.5))
for k in range(n):
    circle()
    t.setheading(0)
    t.left((k+1) * 360/n)
