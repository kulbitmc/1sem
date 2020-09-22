import turtle as t
import numpy as np
t.speed(200)
for i in range(1000):
    t.forward(0.5+np.pi/180*i)
    t.left(2)
