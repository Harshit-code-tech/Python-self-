import time
import math
from turtle import *

def heart(k):
    return 15 * math.sin(k) ** 3

def heart1(k):
    return 12 * math.cos(k) - 5 * \
        math.cos(2 * k) - 2 * \
        math.cos(3 * k) - \
        math.cos(4 * k)

speed(1000)
bgcolor("black")

start_time = time.time()

for i in range(6000):
    penup()
    goto(heart(i) * 20, heart1(i) * 20)
    pendown()

    if time.time() - start_time >= 85:  # 1 minute and 25 seconds
        color("red")
        begin_fill()
        circle(5)
        left(72)
        end_fill()
    else:
        color("purple")
        begin_fill()
        circle(5)
        left(72)
        end_fill()

done()
