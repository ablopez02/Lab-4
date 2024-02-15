import turtle
jack = turtle.Turtle()
jack.color("yellow")

for side in range(4):
    if side==2:
        jack.color("blue")
    jack.forward(100)
    jack.right(90)
    if side==3:
        jack.color("red")
    jack.forward(100)
    jack.right(90)
    if side==4:
        jack.color("yellow")
    jack.forward(100)
    jack.right(90)
    
