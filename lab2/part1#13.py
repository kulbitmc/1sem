mport turtle as t
import numpy as np

def circle(d):
    for i in range(360):
        t.left(1)
        t.forward(d*0.5*np.sin(0.5))
        
t.pencolor('#ffeea8')
t.fillcolor('#ffeea8')
t.begin_fill()
circle(8)
t.end_fill()
t.penup()

t.pencolor('black')
t.fillcolor('white')
t.begin_fill()
t.goto(50,80)
t.pendown()
circle(2)
t.end_fill()
t.penup()

t.goto(-50,80)
t.pendown()
t.begin_fill()
circle(2)
t.end_fill()
t.penup()

t.fillcolor('black')
t.goto(50,100)
t.pendown()
t.begin_fill()
circle(0.5)
t.end_fill()
t.penup()

t.goto(-50,100)
t.pendown()
t.begin_fill()
circle(0.5)
t.end_fill()
t.penup()

t.goto(0,20)
t.pensize(3)
t.pendown()
for i in range(60):
    t.left(1)
    t.forward(6*0.5*np.sin(0.5))
t.penup()
t.goto(0,20)
t.pendown()
t.setheading(180)
for i in range(60):
    t.right(1)
    t.forward(6*0.5*np.sin(0.5))
