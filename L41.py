import turtle
jack = turtle.Turtle()
jack.color("yellow")

for side in range(4):
    if side==3:
        jack.color("blue")
    jack.forward(100)
    jack.right(90)
#the if statement changes the color
