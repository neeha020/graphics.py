import turtle as tur
import colorsys as cs

# Setup
tur.setup(800, 800)
tur.bgcolor("black")
tur.speed(0)
tur.width(2)

# Main pattern
for j in range(25):
    for i in range(15):
        tur.color(cs.hsv_to_rgb(i / 15, j / 25, 1))
        tur.right(90)
        tur.circle(200 - j * 4, 90)
        tur.left(90)
        tur.circle(200 - j * 4, 90)
        tur.right(180)
        tur.circle(50, 24)

# Center black circle
center = tur.Turtle()
center.hideturtle()
center.penup()
center.goto(0, -20)
center.pendown()
center.color("black")
center.begin_fill()
center.circle(20)
center.end_fill()

# Background starburst
bg = tur.Turtle()
bg.speed(0)
bg.hideturtle()
bg.width(1)

for angle in range(0, 360, 5):
    bg.penup()
    bg.goto(0, 0)
    bg.setheading(angle)
    bg.pencolor(cs.hsv_to_rgb(angle / 360, 0.3, 0.3))
    bg.forward(300)
    bg.pendown()
    bg.forward(20)

# White overlay petals
outline = tur.Turtle()
outline.speed(0)
outline.width(0.5)
outline.color("white")
outline.hideturtle()

for j in range(25):
    for i in range(15):
        outline.penup()
        outline.goto(0, 0)
        outline.setheading(0)
        outline.right(90)
        outline.circle(200 - j * 4, 90)
        outline.left(90)
        outline.pendown()
        outline.circle(200 - j * 4, 90)
        outline.right(180)
        outline.circle(50, 24)

# Extra Feature: Colorful glow rings
glow = tur.Turtle()
glow.speed(0)
glow.hideturtle()
glow.width(3)

for r in range(220, 320, 20):
    glow.penup()
    glow.goto(0, -r)
    glow.pendown()
    hue = (r % 360) / 360
    glow.color(cs.hsv_to_rgb(hue, 1, 0.4))
    glow.circle(r)

# Extra Feature: Rainbow outer border
border = tur.Turtle()
border.speed(0)
border.hideturtle()
border.width(10)
border.penup()
border.goto(0, -390)
border.pendown()
border.color("white")
border.begin_fill()
border.circle(390)
border.end_fill()

rainbow = tur.Turtle()
rainbow.speed(0)
rainbow.hideturtle()
rainbow.width(4)
for i in range(360):
    rainbow.penup()
    rainbow.goto(0, -390)
    rainbow.setheading(i)
    rainbow.forward(390)
    rainbow.pendown()
    rainbow.pencolor(cs.hsv_to_rgb(i / 360, 1, 1))
    rainbow.forward(5)

# Finalize
tur.hideturtle()
tur.done()
