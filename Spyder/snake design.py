from turtle import *
bgcolor('black')
speed(0)
hideturtle()
for i in range(180):
    color('green')
    circle(i*0.3)
    color('blue')
    circle(i*0.2)
    right(3)
    forward(3)
done()
