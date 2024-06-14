import turtle

t=turtle.Turtle()
window=turtle.Screen()
window.bgcolor('black')
window.screensize(1920,1080)
window.setup(width=1.0, height=1.0,startx=None ,starty=None)
t.pencolor('green')
t.pen(pencolor="white",fillcolor="cyan", pensize=3, speed=8)


t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=2)
t.begin_fill()
t.penup()
t.goto(-300,300)
t.pendown()

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


t.penup()
t.fd(140)

t.fd(70)


t.pen(pencolor="white",fillcolor="cyan", pensize=3, speed=8)
t.begin_fill()

t.rt(800)
t.fd(190)
t.lt(90)
t.pendown()
t.circle(100)
t.end_fill()

t.pen(pencolor="white",fillcolor="black", pensize=3, speed=8)
t.begin_fill()
t.lt(50)
t.penup()
t.fd(50)
t.rt(20)
t.pendown()
t.circle(70)
t.rt(110)
t.end_fill()


t.penup()
t.fd(30)
t.lt(80)
t.fd(90)
t.pendown()

t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=8)
t.begin_fill()

t.lt(100)
t.fd(120)
t.rt(100)
t.fd(20)
t.rt(80)
t.fd(100)
t.lt(80)
t.fd(20)
t.lt(80)
t.fd(100)
t.rt(80)
t.fd(20)
t.rt(100)
t.fd(120)
t.rt(80)
t.fd(50)
t.lt(180)

t.end_fill()


t.penup()

t.fd(100)
t.pendown()


t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=8)
t.begin_fill()

t.lt(90)
t.fd(120)
t.rt(90)
t.fd(80)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(60)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(60)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(60)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(60)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(80)

t.end_fill()