import turtle
from random import randint

WIDTH = 950
HEIGHT = 950

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.tracer(200)
screen.bgcolor("black")

Tip = 0.0001

T = turtle.Turtle()
T.color("white")
T.pensize(1)
T.shapesize(stretch_wid=Tip, stretch_len=Tip)

side = 20
iterations = 10000

for i in reversed(range(iterations)):

    value = randint(1, 2)
    x, y = T.pos()
    a = (i / iterations) ** (1 / 3)

    T.pencolor(1 - abs(a), 1 - abs(a), 1 - abs(a))

    if abs(x) > WIDTH:
        T.penup()
        T.goto(0.0, 0.0)
        T.pendown()
    if abs(y) > HEIGHT:
        T.penup()
        T.goto(0.0, 0.0)
        T.pendown()

    if value <= 1:
        T.rt(60)
        T.forward(side * 0.5)
    else:
        T.lt(60)
        T.forward(side)

screen.exitonclick()
