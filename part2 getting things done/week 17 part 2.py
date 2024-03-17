# D = v**2 * (sin(2x)) / g
# Noah is playing with his Maya. What happened Noah threw a ball 
# noah wants to find the angle on which if he threw ball the ball
# will cover maximum distance

import math
v = 10#m/s
g = 9.8#m/sq


x = math.radians(90)
d = v**2 * (math.sin(2*x)) / g
print(d,x)






for x in range(90):
    theta = math.radians(x)
    d = v**2 * (math.sin(2*theta)) / g
    print(d,x)





x = math.radians(45)
d = v**2 * (math.sin(2*x)) / g
print(f'the best angel is {45} because we have {d} distance coverered on this angle')
