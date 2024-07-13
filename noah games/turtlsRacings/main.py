import turtle as tt
import time

noah = tt.Turtle()
noah.shape('turtle')
noah.color('blue')
noah.penup()

umair = tt.Turtle()
umair.shape('turtle')
umair.color('red')
umair.penup()

noah.goto(-500,300)
umair.goto(-500,-300)
from random import randint


while True:
    time.sleep(0.01)
    if randint(1,10) ==7:
        noah.circle(50)
    if randint(1,10) ==4:
        umair.circle(50)
    
    noah.forward(randint(1,10))
    umair.forward(randint(1,10))

    if noah.xcor() > 500 or umair.xcor() > 500:
        if noah.xcor() > umair.xcor():
            tt.write('noah wins', align='center', font=('Arial', 40, 'normal'))
        else:
            tt.write('umair wins', align='center', font=('Arial', 40, 'normal'))
    


tt.mainloop()
