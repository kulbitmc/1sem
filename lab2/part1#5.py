import turtle as t
t.shape('turtle')
t.penup()
t.goto (-50, -50)
t.pendown()
def square (x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.penup()
    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.pendown()
def func (x):
        for i in range (10):
            square (x)
            x+= 20
func(50)
input()
