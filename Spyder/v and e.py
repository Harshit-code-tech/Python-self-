import turtle

t=turtle.Turtle()
window=turtle.Screen()
window.bgcolor('black')
window.screensize(1920,1080)
window.setup(width=1.0, height=1.0,startx=None ,starty=None)
t.pencolor('green')
t.penup()
t.goto(-300,300)
t.pendown()

t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=2)
t.begin_fill()

t.rt(90)
t.fd(25)
t.rt(90)
t.fd(165)
t.lt(90)
t.fd(115)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(140)
t.rt(90)
t.fd(190)
t.rt(90)

t.end_fill()
# End of 'L'

t.penup()
t.fd(140)

#Gap between 'L' and 'O'
t.fd(70)
t.pendown()

t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=2)
t.begin_fill()

t.lt(90)
t.fd(70)
t.lt(30)
t.fd(100)
t.rt(120)
t.fd(40)
t.rt(60)
t.fd(80)
t.lt(180)
t.rt(60)
t.fd(60)
t.rt(60)
t.fd(20)
t.rt(120)
t.fd(80)
t.lt(30)
t.fd(50)
t.rt(90)
t.fd(20)
t.rt(180)

t.end_fill()