import turtle


class Ball(turtle.Turtle):
    def __init__(self, color, x, y):
        super().__init__()
        self.shape("circle")
        self.color(color)
        self.penup()
        self.x = x
        self.y = y
        self.goto(x, y) 

    def move_ball(self):
        self.x = self.x + 1
        self.y = self.y + 1
        self.goto(self.x, self.y)

    def ball_bounce_y(self):
        self.x = self.x * -1

    def ball_bounce_x(self):
        self.y = self.y * -1





if __name__ == "__main__":
    ball = Ball("red", 200, 0)
    while(True):
        ball.move_ball()
        if ball.ycor() > 400 or ball.ycor() < -400:
            ball.ball_bounce_y()
        if ball.xcor() > 400 or ball.xcor() < -400:
            ball.ball_bounce_x()

