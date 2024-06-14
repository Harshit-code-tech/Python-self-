from turtle import *

# First code: Drawing Om symbol between four diyas
bgcolor("white")
speed(10)
width(40)
pencolor("orangered")
penup()
setpos(-200, 150)
pendown()
left(60)
circle(-120, 230)
bgcolor("grey")
left(160)
circle(-130, 230)
fd(180)
bgcolor("black")
penup()
setpos(-20, -24)
pendown()
left(60)
circle(90, -80)
bgcolor("Violet")
fd(-130)
circle(-70, -170)
back(320)
circle(-70, -170)
back(190)
bgcolor("orange")
penup()
setpos(-60, 300)
pendown()
rt(170)
circle(120, 160)
bgcolor("skyblue")
penup()
setpos(90, 270)
pendown()
circle(30, 360)
color("black")
penup()

clear()
# Second code: Birthday-themed animation

import turtle
import datetime
import time
import random

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Happy Birthday!")
screen.bgcolor("black")

# Create a turtle object
t = turtle.Turtle()
t.width(2)
t.speed(1)


# Function to draw a diya
def draw_diya(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("yellow", "red")
    t.begin_fill()
    t.forward(30)
    t.left(120)
    t.forward(30)
    t.left(120)
    t.forward(30)
    t.left(120)
    t.end_fill()
    t.penup()


# Function to play the birthday song
# def play_birthday_song():
#     song_path = "/home/harshitghosh/Music/Middle time songs/Happy Birthday To You Ji.mp3"  # Replace with the path to your birthday song file
#     subprocess.Popen(["xdg-open", song_path])
# Function to draw party bombs
def draw_party_bomb(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("orange", "red")
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.penup()


# Function to write the birthday message
def write_message(message, x, y, font_size, color, animated=False):
    t.color(color)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(message, align="center", font=("Arial", font_size, "bold"))
    t.penup()

    if animated:
        time.sleep(0.5)


# Function to draw balloons
def draw_balloons(num_balloons):
    colors = ["red", "blue", "yellow", "green", "purple", "orange"]
    for _ in range(num_balloons):
        x = random.randint(-screen.window_width() // 2, screen.window_width() // 2)
        y = random.randint(-screen.window_height() // 2, screen.window_height() // 2)
        color = random.choice(colors)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color("black", color)
        t.begin_fill()
        t.circle(20)
        t.end_fill()


# Function to sprinkle confetti
def sprinkle_confetti(num_confetti):
    colors = ["red", "blue", "yellow", "green", "purple", "orange"]
    for _ in range(num_confetti):
        x = random.randint(-screen.window_width() // 2, screen.window_width() // 2)
        y = random.randint(-screen.window_height() // 2, screen.window_height() // 2)
        color = random.choice(colors)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(5, color)
        time.sleep(0.05)  # Reduce the delay for faster animation


# Function to create banners
def create_banners(num_banners):
    colors = ["red", "blue", "yellow", "green", "purple", "orange"]
    for _ in range(num_banners):
        x = random.randint(-screen.window_width() // 2, screen.window_width() // 2)
        y = random.randint(-screen.window_height() // 2, screen.window_height() // 2)
        color = random.choice(colors)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color(color)
        t.write("जन्मदिन की शुभकामनाएँ!,Mera Briyani and mango shake???", align="center", font=("Arial", 24, "bold"))


# Function to draw party hats
def draw_party_hats(num_hats):
    colors = ["red", "blue", "yellow", "green", "purple", "orange"]
    for _ in range(num_hats):
        x = random.randint(-screen.window_width() // 2, screen.window_width() // 2)
        y = random.randint(-screen.window_height() // 2, screen.window_height() // 2)
        color = random.choice(colors)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color(color)
        t.begin_fill()
        t.goto(x + 20, y + 50)
        t.goto(x + 40, y)
        t.goto(x, y)
        t.end_fill()


# Function to add sparkle effects
def add_sparkles(num_sparkles):
    colors = ["red", "blue", "yellow", "green", "purple", "orange"]
    for _ in range(num_sparkles):
        x = random.randint(-screen.window_width() // 2, screen.window_width() // 2)
        y = random.randint(-screen.window_height() // 2, screen.window_height() // 2)
        color = random.choice(colors)
        t.penup()
        t.goto(x, y)
        t.pendown()
        for _ in range(6):
            t.color(color)
            t.forward(10)
            t.backward(10)
            t.right(60)


# Main program
def main():
    # Start playing the birthday song in the background
    # song_thread = threading.Thread(target=play_birthday_song)
    # song_thread.start()

    # Draw burning diyas
    draw_diya(-300, -300)
    draw_diya(-300, 300)
    draw_diya(300, -300)
    draw_diya(300, 300)
    time.sleep(2)

    # Clear the screen
    t.clear()

    # Draw party bombs
    draw_party_bomb(-200, -100)
    draw_party_bomb(-100, 0)
    draw_party_bomb(100, 0)
    draw_party_bomb(200, -100)

    # Hide the turtle
    t.hideturtle()

    # Change the background to pink
    screen.bgcolor("pink")

    # Write the birthday message
    write_message("जन्मदिन की", 0, -250, 40, "red", animated=True)
    write_message("हार्दिक शुभकामनाएँ,", 0, -300, 40, "red", animated=True)
    write_message("माँ!", 0, -350, 40, "red", animated=True)
    write_message("आपका दिन खुशियों से भरा रहे,", 0, -400, 18, "purple", animated=True)
    write_message("प्यार, और हँसी!", 0, -430, 18, "purple", animated=True)

    # Get the current time
    current_time = datetime.datetime.now().strftime("%I:%M %p")

    # Write the current time
    write_message("Current time: " + current_time, 0, -480, 18, "blue", animated=True)

    # Create a turtle object (pen)
    pen = turtle.Turtle()
    pen.ht()  # Hide the turtle

    # Adjust the turtle position to match the expected output
    pen.penup()
    pen.goto(0, 250)
    pen.pendown()

    # Draw decorations
    draw_balloons(5)
    sprinkle_confetti(10)  # Adjusted the number and reduced the delay for faster animation
    create_banners(3)
    draw_party_hats(5)
    add_sparkles(10)  # Adjusted the number for faster animation

    # Define method to draw curve
    def curve():
        for i in range(200):
            pen.right(1)
            pen.forward(1)

    # Define method to draw a full heart
    def heart():
        pen.fillcolor('red')
        pen.begin_fill()
        pen.left(140)
        pen.forward(113)
        curve()
        pen.left(120)
        curve()
        pen.forward(112)
        pen.end_fill()

    # Draw a heart
    heart()

    # Write text inside the heart with an animated effect
    def txt():
        pen.up()
        pen.goto(0, 350)
        pen.down()
        pen.color('lightgreen')
        pen.write("", align="center", font=("Verdana", 12, "bold"))

        message = "Love you, Mom!"
        for i in range(1, len(message) + 1):
            pen.undo()
            pen.write(message[:i], align="center", font=("Verdana", 12, "bold"))
            time.sleep(0.3)

    # Write text inside the heart
    txt()

    # Close the turtle graphics window after a delay

    time.sleep(5)
    song_thread.join()
    screen.bye()


# Run the program
if __name__ == "__main__":
    main()
