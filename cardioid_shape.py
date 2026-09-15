"""import math

def draw_cardioid_outline(width = 60, height = 30):

    grid =[[" " for _ in range(width)] for _ in range(height)]

    for angle_deg in range(360):
        theta = math.radians(angle_deg)
        r = 1 + math.cos(theta)
        x = r * math.cos(theta)
        y = r * math.sin(theta)

        col = int((x - (-0.5)) / (2.2 - (-0.5)) * (width - 1)) 
        row = int((y - (-1.5)) / (1.5 - (-1.5)) * (height - 1))
        row =  (height - 1) - row
        if 0 <= col < width and 0 <= row < height:
            grid[row][col] = "*"

    for row in grid:
        print("".join(row))
draw_cardioid_outline()"""

import colorsys
import math
import turtle

def dessiner_cardioide():
    screen = turtle.Screen()
    screen.setup(width = 800, height=800)
    screen.title("Cardioïde avec Turtle et Colorsys")
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    t.width(3)
    t.hideturtle()
    echelle = 150
    t.penup()

    for angle_deg in range(361):
        theta = math.radians(angle_deg)
        r = 1 + math.cos(theta)
        x = r * math.cos(theta) * echelle
        y = r * math.sin(theta) * echelle
        teinte = angle_deg / 360.0

        rgb = colorsys.hls_to_rgb(teinte, 0.5, 1.0)
        t.pencolor(rgb)
        t.goto(x,y)
        if angle_deg == 0:
            t.pendown()
    screen.mainloop()

if __name__ == "__main__":
    dessiner_cardioide()

