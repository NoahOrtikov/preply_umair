import turtle
import random
class Car:
    def __init__(self, x, y):
        self.car = turtle.Turtle()
        self.car.shape("square")
        self.car.color("red")
        self.car.penup()
        self.car.goto(x, y)
        self.car.shapesize(2, 2)
        self.car.left(90)

    def move_car(self, x, y):
        self.car.setposition(x, y)

    def destroy_car(self):
        self.car.hideturtle()
    
    def move_forward(self):
        if self.car.ycor() <= 400   :
            self.car.forward(20)

    def move_backward(self):
        if self.car.ycor() >= -400   :
            self.car.backward(20)





class randomCars():
    def __init__(self):
        self.colors = ["red", "blue", "green", "yellow", "purple"]
        self.shapes = ["square", "triangle", "circle",'turtle']
       
        self.cars = [] 
        self.create_cars()
    def create_cars(self):
        if random.randint(1, 100) == 7:
            for _ in range(5):
                tt = turtle.Turtle()
                tt.penup()
                tt.goto(random.randint(400, 400), random.randint(-500, 500))   
                tt.shape(random.choice(self.shapes))
                tt.color(random.choice(self.colors))
                self.cars.append(tt)

        return self.cars
    
    def move_cars(self,speed = 12):
        for car in self.cars:
            car.backward(speed)
            if car.xcor() < -400:
                self.cars.remove(car)

    def  detect_collision(self, player):
        for car in self.cars:
            if abs(player.xcor() - car.xcor()) < 20 and abs(player.ycor() - car.ycor()) < 20:
                return True
        
   
