"""Module de dessin de cardioïde avec Turtle."""

import colorsys
import math
import turtle


def dessiner_cardioide() -> None:
    """Trace une cardioïde colorée."""
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
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
        t.goto(x, y)
        if angle_deg == 0:
            t.pendown()
    screen.mainloop()


if __name__ == "__main__":
    dessiner_cardioide()
