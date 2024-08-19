import turtle
import random


ball = turtle.Turtle()
ball.color("red")
ball.shape("circle")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5


while(True):
    ball.setx(ball.xcor() + 5)
    ball.sety(ball.ycor() + 5)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

turtle.mainloop()