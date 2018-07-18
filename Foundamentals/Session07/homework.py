
# Hello World
for i in range (3) :
    print("Hello world")


# Sum
x = 2
y = 3
sum = x + y
print(sum)

# Square
# from turtle import *
# shape ("turtle")
# color ("red")
# speed (-1)
# for i in range (4) :
#     forward (100)
#     left (90)
# mainloop()

# 4
# from turtle import *
# def draw_square(x,y): 
#     speed(-1)  
#     color(y)
#     for i in range(4):
#         forward(x)
#         left(90) 
# for i in range(30):
#     draw_square(i * 5, 'red')
#     left(17)
#     penup()
#     forward(i * 2)
#     pendown()    
# mainloop()    

# draw_star
# from turtle import *
# def draw_star(x,y,lenght):
#     penup()
#     goto(x,y)
#     pendown()
#     for i in range(5):
#         forward(lenght)
#         right(144)
# speed(0)
# color('blue')
# for i in range(100):
#     import random
#     x = random.randint(-300, 300)
#     y = random.randint(-300, 300)
#     length = random.randint(3, 10)
#     draw_star(x, y, length)
# mainloop()

# remove_dollar_sign 
def remove_dollar_sign(s) :
    string = s.replace("$","")
    return string 

string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up" :
    print("your function is correct")
else :
    print("There's a bug")

# get even list
def get_even_list (a) :
    for number in a :
        if number % 2 != 0 :
            a.remove(number)
    return (a)

even_list = get_even_list ([1,2,5,-10,9,6])

if set (even_list) == set ([2,10,-6]) :
    print ("correct")
else :
    print("ooops,bugs detected")


