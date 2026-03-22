import turtle

t = turtle.Turtle()
t.speed(3)

def drawSquare(length,angle):
    for i in range(4):
        t.forward(length)
        t.right(angle)

drawSquare(100,90)
turtle.done()