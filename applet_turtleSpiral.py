import turtle

WIDTH = 950
HEIGHT = 950

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.tracer(2)
screen.bgcolor("black")

buffer = (WIDTH / 2) - WIDTH * 0.05
Tip = 0.0001

T = turtle.Turtle()
T.color("white")
T.pensize(2)
T.penup()
T.goto(-buffer, buffer)
T.pendown()

T.shapesize(stretch_wid=Tip, stretch_len=Tip)

for i in range(80):
    T.rt(i)
    T.forward(80 - i)

screen.exitonclick()
