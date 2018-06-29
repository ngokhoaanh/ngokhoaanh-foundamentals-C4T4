# Turtle1
# from turtle import*
# speed(-1)
# color("green")
# shape("turtle")

# for _ in range (100):

#     left (10)
#     for i in range (4) :
#         forward(100)
#         left (90)


    
# mainloop()

from turtle import*
speed(-1)
color("green")
shape("turtle")
for i in range (20):
    for _ in range (4) :
        forward(10 + i * 10)
        left (90)
    left(10)

mainloop()

