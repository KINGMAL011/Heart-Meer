import math
from turtle import *

def heart(k):
    return 15 * math.sin(k)**3

def heart1(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(0) 
bgcolor('pink')
penup()
goto(0, 0)
pendown()

begin_fill()
color("red")
for i in range(360):
    k = math.radians(i)
    x = heart(k) * 10
    y = heart1(k) * 10
    goto(x, y)
end_fill()

penup()
goto(0, -10) 
pendown()
color("white")
write("Meer", align="center", font=("Arial", 24, "bold"))

done()
