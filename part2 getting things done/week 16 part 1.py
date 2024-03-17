'task1 make a list of 5 colors'
import turtle
import random
turtle.speed('fastest')
s = ['red','orange','yellow','green','blue']
'intask2 write a for loop for range(4'
turtle.pensize(2)
step = 10
# task 10 make a list of degree 0 90 180 270 and then use turle.left(random.choice(lst))
#task8: write a for loop till 100
lst = [0 , 90,180,270]
for a in range(100):
    for i in range(4):# before for loop write a variable step and assign it value 100
        # task 4 move turtle forward fo rsteps using turtle.foward(step) and turn left ad assing it 90 ang;e
        turtle.forward(step)
        turtle.left(random.choice(lst))
        #task 6 is import random moduel and write random.choice(s)
        rc = random.choice(s)
        # task 7: turtle.color(rc)
        turtle.color(rc)
    #task 9 write a angle left 5
    

# task five close the turtle process bu wrting turtle.mainloop
turtle.mainloop()
 
