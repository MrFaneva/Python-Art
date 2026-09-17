"""Module de génération de spirale arc-en-ciel."""

import colorsys
import turtle

# Screen setup
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)

n = 36
h = 0.0

# Generating the viral loop

for i in range(300):
    c = colorsys.hsv_to_rgb(h, 1.0, 1.0)
    h += 1 / n
    t.color(c)
    t.forward(i * 2)
    # The magic angle for the spiral:
    # 60 for hexagonal, 90 for square, 120 for triangular.
    t.left(60)
    t.width(int(i / 100 + 1))

turtle.done()
