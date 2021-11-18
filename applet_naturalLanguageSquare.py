import turtle
from random import randint

# Set up canvas.

screen = turtle.Screen()
screen.setup(945, 945)
screen.bgcolor("black")

# Set up turtle pentip.

turtle.shapesize(stretch_wid=0.0001, stretch_len=0.0001)
turtle.color("white")
turtle.speed(999)
turtle.penup()

# Natural language distribution of letters in English texts.

E = "E" * 1300
T = "T" * 910
A = "A" * 820
O = "O" * 750
I = "I" * 700
N = "N" * 670
S = "S" * 630
H = "H" * 610
R = "R" * 600
D = "D" * 430
L = "L" * 400
C = "C" * 280
U = "U" * 280
M = "M" * 240
W = "W" * 240
F = "F" * 220
G = "G" * 200
Y = "Y" * 200
P = "P" * 190
B = "B" * 150
V = "V" * 98
K = "K" * 77
X = "X" * 15
J = "J" * 15
Q = "Q" * 10
Z = "Z" * 7

letters = A + B + C + D + E + F + G + H + I + J + K + L + M
letters += N + O + P + Q + R + S + T + U + V + W + X + Y + Z

# Convert the natural language distribution of letters into
# an array (nested list) that turtle can use to populate the
# rendered matrix. First rows `i`, then columns `j`.

matrixSide = 33
width = 360 * -1
height = 360 * -1
matrixLength = (width * 2) * -1

letterMatrix = []

for i in range(matrixSide):
    letterRow = []
    for j in range(matrixSide):
        index = randint(0, len(letters) - 1)
        letterRow.append(letters[index])
    letterMatrix.append(letterRow)

# Using `letterMatrix`, turtle will populate each cell of the matrix
# with a letter, one at a time. First by row `i`, then by column `j`.

y = height + matrixLength / (2 * matrixSide) - 1

for i in range(matrixSide):

    x = width + matrixLength / (2 * matrixSide) - 1

    for j in range(matrixSide):
        turtle.goto(x, y)
        turtle.write(
            letterMatrix[i][j],
            align="right",
            font=("Consolas", 13, "normal"),
        )

        x += matrixLength / matrixSide

    y += matrixLength / matrixSide

turtle.color("black")
turtle.done()
