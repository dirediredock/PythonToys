import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(945, 945)

T = turtle.Turtle()
T.shapesize(stretch_wid=0.0001, stretch_len=0.0001)
T.color("white")
T.speed(10000)

for i in range(1000):  # 245
    T.forward(i * 4)
    T.left(120.11)

turtle.done()
