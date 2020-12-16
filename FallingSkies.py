# Falling Skies game
# Made By Ansh Kataria
# Date 6 December 2020

import turtle
import random

# game over or not
game_still_going = True

# Score
score = 0

# Number of lives
lives = 50

# Setup The Screen
screen = turtle.Screen()
screen.title("Falling Skies")
screen.bgpic("background.gif")
screen.setup(width=800, height=600)
screen.tracer(0)

# Register shapes
screen.register_shape("deer_right.gif")
screen.register_shape("deer_left.gif")
screen.register_shape("food.gif")
screen.register_shape("hunter.gif")

# Add the player
player = turtle.Turtle()
player.speed(0)
player.shape("deer_right.gif")
player.penup()
player.goto(0, -250)
player.direction = "stop"

# Food list
foods = []

# Add the Food
for _ in range(20):
    food = turtle.Turtle()
    food.speed(0)
    food.shape("food.gif")
    food.penup()
    food.goto(random.randint(-290, 290), 250)
    food.speeds = random.randint(1, 3)
    foods.append(food)

# Hunters list
hunters = []

# Add the hunter
for _ in range(20):
    hunter = turtle.Turtle()
    hunter.speed(0)
    hunter.shape("hunter.gif")
    hunter.penup()
    hunter.goto(random.randint(-290, 290), 250)
    hunter.speeds = random.randint(1, 3)
    hunters.append(hunter)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.write("Score: {} Lives: {} ".format(score, lives), align="center", font=("courier", 24, "normal"))


# Functions
def go_left():
    player.direction = "left"
    player.shape("deer_left.gif")


def go_right():
    player.direction = "right"
    player.shape("deer_right.gif")


# Game ending
def end_game(Current_lives):
    global game_still_going
    if Current_lives < 0:
        game_still_going = False
        screen.clear()


# Key bindings
screen.listen()
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Main game loop
while game_still_going:
    # Update the screen
    screen.update()

    # Check Borders
    if player.xcor() < -390:
        player.setx(390)

    if player.xcor() > 390:
        player.setx(-390)

    # Move the player
    if player.direction == "left":
        x = player.xcor()
        x -= 2
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 2
        player.setx(x)

    # Move the food
    for food in foods:
        # Move down the food
        y = food.ycor()
        y -= food.speeds
        food.sety(y)

        # Check if it is of the screen
        if y < -290:
            x = random.randint(-280, 280)
            y = random.randint(240, 250)
            food.goto(x, y)

        # Check for the collision with the player
        if food.distance(player) < 30:
            x = random.randint(-280, 280)
            y = random.randint(240, 250)
            food.goto(x, y)
            score += 10
            pen.clear()
            pen.write("Score: {} Lives: {} ".format(score, lives), align="center", font=("courier", 24, "normal"))

    # Move the hunters
    for hunter in hunters:
        # Move down the hunter
        y = hunter.ycor()
        y -= hunter.speeds
        hunter.sety(y)

        # Check if it is of the screen
        if y < -290:
            x = random.randint(-280, 280)
            y = random.randint(240, 250)
            hunter.goto(x, y)

        # Check for the collision with the player
        if hunter.distance(player) < 30:
            x = random.randint(-280, 280)
            y = random.randint(240, 250)
            hunter.goto(x, y)
            lives -= 1
            end_game(lives)
            pen.clear()
            pen.write("Score: {} Lives: {} ".format(score, lives), align="center", font=("courier", 24, "normal"))

# Game over message
message = turtle.Screen()
message.bgpic("game_over.gif")
message.setup(width=500, height=364)
message.tracer(0)

while True:
    # updating the screen
    message.update()
