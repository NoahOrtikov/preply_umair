import turtle


class Brick(turtle.Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=3)
        self.goto(x, y)

if __name__ == "__main__":
    list_of_x_position= [-400,-300, -200, -100, 0, 100, 200, 300,400]
    for i in range(100,500,50):
        for j in list_of_x_position:
            Brick(j, i, "red")
    turtle.mainloop()