import turtle
from random import randint

WIDTH = 950
HEIGHT = 950

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.tracer(300)
screen.bgcolor("black")

Tip = 0.0001
T = turtle.Turtle()
T.shapesize(stretch_wid=Tip, stretch_len=Tip)
T.color("white")
T.pensize(0.1)

def draw_oval(x, y, big_radius, small_radius, tilt):
    T.up()
    T.goto(x, y)
    T.down()
    T.seth(-45 + tilt)
    T.circle(big_radius, 90)
    T.circle(small_radius, 90)
    T.circle(big_radius, 90)
    T.circle(small_radius, 90)

for i in range(10000):
    for x in range(100):
        T.forward(1 + i / 20)
        T.left((30 + x) - i / 30)

turtle.done()
