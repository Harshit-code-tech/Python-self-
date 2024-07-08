import turtle
import time
t=turtle.Turtle()
window=turtle.Screen()
window.bgcolor('black')
window.screensize(1920,1080)
window.setup(width=1.0, height=1.0,startx=None ,starty=None)
def curve():
    t.pen(pencolor="white", pensize=3, speed=5)
    for i in range(200):
        t.rt(1)
        t.fd(1)

def love_sign():
    t.pen(pencolor="white",fillcolor="hot pink", pensize=3, speed=5)
    t.shape("turtle")
    t.shapesize(1,1,1)
    t.begin_fill()
    t.lt(50)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(112)
    t.end_fill()

    t.hideturtle()

love_sign()

time.sleep(5)