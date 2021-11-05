import turtle

WIDTH = 950
HEIGHT = 950

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.tracer(200)
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

for i in range(200):
    draw_oval(0, 0, 10 * i, 10 * i, 0)

print("Done!")

screen.exitonclick()
