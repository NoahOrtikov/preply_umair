import turtle as t 

t1 = t.Turtle()

t1.color('red')
for i in range(100,0,-10):
    t1.forward(i)
    t1.left(90)



# question2 make another turtle of color red its name will t2 and it will move 0 to 1000 with step size of 5

t2 = t.Turtle()
t2.speed('fastest')
t2.color('red')
for i in range(0,1000,5):
    t.forward(i)
    t.left(90)



t.mainloop()


