import turtle as t
t.shape('classic')
n = int(input())
a = int(input())
for i in range(n+3):
    i += 3
    q = float(180 - 360/i)
    for k in range(i):
        if k == 0:
            t.left(180 - q/2)
        else:
            t.left(180 - q)
        t.forward(a + a * i)
    t.penup()
    t.setheading(0)
    t.forward(a)
    t.pendown()
