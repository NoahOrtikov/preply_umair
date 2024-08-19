import turtle
import random
import time

# Set up the screen
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("yellow")
win.setup(width=800, height=800)
win.tracer(0)  # Turns off the screen updates

# Snake head
snake_head = turtle.Turtle()
snake_head.shape("square")
snake_head.color("green")
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = "stop"

# Apple
apple = turtle.Turtle()
apple.shape("circle")
apple.color("red")
apple.shapesize(1.5, 1.5)
apple.penup()
apple.goto(random.randint(-800, 800), random.randint(-800, 800))

# Functions
def move_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"

def move_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"

def move_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"

def move_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"

def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y + 20)

    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y - 20)

    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x - 20)

    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x + 20)

# Keyboard bindings
win.listen()
win.onkey(move_left, "Left")
win.onkey(move_right, "Right")
win.onkey(move_up, "Up")
win.onkey(move_down, "Down")

# Main game loop
score = 0
turtle.tracer(0)
while True:
    win.update()
    move()

    # Check for collision with the border
    if snake_head.xcor() > 800 or snake_head.xcor() < -800 or snake_head.ycor() > 800 or snake_head.ycor() < -800:
        time.sleep(1)
        snake_head.goto(0, 0)
        snake_head.direction = "stop"
        score = 0

    # Check for collision with the apple
    if snake_head.distance(apple) < 20:
        score += 1
        apple.goto(random.randint(-30, 30), random.randint(-30, 30))

    # Clear previous score display
    turtle.clear()
    turtle.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    time.sleep(0.1)

win.mainloop()
