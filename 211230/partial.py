import turtle
import random
import time
from pygame import mixer

width = height = 500

window = turtle.Screen()
window.setup(width, height)
window.bgcolor("sky blue")
window.title("Happy Holidays")

snowball_rate = 1, 3
snowball_size = 5, 15
wind_change = 1, 5
max_wind = 3


# Create all circle-shaped objects
def make_circle(turtle_name, x, y, size, colour):
    turtle_name.color(colour)
    turtle_name.penup()
    turtle_name.setposition(x, y)
    turtle_name.dot(size)


list_of_snowballs = []


def make_snowball():
    snowball = turtle.Turtle()
    snowball.color("white")
    snowball.penup()
    snowball.setposition(random.randint(-2 * width, width / 2), height / 2)
    snowball.hideturtle()
    snowball.size = random.randint(*snowball_size)
    list_of_snowballs.append(snowball)


def move_snowball(turtle_name, falling_speed=1, wind=0):
    turtle_name.clear()
    turtle_name.sety(turtle_name.ycor() - falling_speed)
    if wind:
        turtle_name.setx(turtle_name.xcor() + wind)
    turtle_name.dot(turtle_name.size)


snowman = turtle.Turtle()
x_position = 0
y_positions = 75, 0, -100
size = 75
for y in y_positions:
    make_circle(snowman, x_position, y, size, "white")
    size = size * 1.5
