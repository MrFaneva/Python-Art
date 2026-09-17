"""Module de génération d'effet solaire géométrique."""

import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
turtle.tracer(4, 0)

colors = [
    "#FFE0B2",
    "#FFB74D",
    "#FFA726",
    "#FB8C00",
    "#E65100",
]

for i in range(360):
    t.color(colors[i % 5])
    t.circle(140)
    t.left(1)
turtle.done()
