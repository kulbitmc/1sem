import turtle as t
t.shape('classic')
n = int(input())
for i in range(n):
    t.left(360/n)
    t.forward(100)
    t.stamp()
    t.left(180)
    t.forward(100)
    t.left(180)
input()