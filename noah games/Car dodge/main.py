import turtle as noah
from car import Car, randomCars


noahScreen = noah.Screen()
noahScreen.setup(width=800, height=600)
noahScreen.title("Car Dodge")
noahScreen.bgcolor("pink")

noahScreen.tracer(0)
noah.listen(    )
car = Car(0, -300)
noah.onkeypress(car.move_forward, "Up")
noah.onkeypress(car.move_backward, "Down")



cars = randomCars()
i = 0
speed = 1
while True:
    i = i + 1
    if i % 1000 == 0:
        speed = speed + 3
    noahScreen.update()
    cars.create_cars()
    cars.move_cars(speed = speed)
    if cars.detect_collision(car.car):
        break

noah.write("GAME OVER", align="center", font=("Courier", 30, "normal"))
noah.mainloop()