from turtle import *
speed(-1)
shape("turtle")
color("red")
for i in range (100) :
    for _ in range(4) :
        forward(100+i*2)
        left(90)
    right(10)
    forward(10)
mainloop()
