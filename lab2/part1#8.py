import turtle as t
t.shape('classic')
n = int(input())
for i in range(n):
    t.forward(10 + i * 10)
    t.left(90)
