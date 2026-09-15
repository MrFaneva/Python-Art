import turtle
import colorsys

#Screen setup
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)

n = 36 # Number of colors
h = 0

# Generating the viral loop

for i in range(300):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 1/n
    t.color(c)
    t.forward(i*2)
    t.left(60) # The magic angle for the spiral, you can change it to see different patterns: 90 for a square spiral, 60 for a hexagonal spiral, 120 for a triangular spiral, etc.
    t.width(i/100+1)

turtle.done()


