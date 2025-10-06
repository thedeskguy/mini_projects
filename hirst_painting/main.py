# import colorgram
# colors=colorgram.extract('/Users/divyanshuagarwal/Desktop/python/hirst_painting/hirst.jpeg', 30)
# rgb_colors=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import random
from turtle import Turtle,Screen,colormode
colormode(255)
timmy=Turtle()
# print(timmy)
color_list=[(246, 242, 234), (248, 241, 245), (239, 247, 242), (239, 242, 247), (198, 164, 115), (145, 79, 54), (222, 202, 136), (57, 93, 122), (170, 154, 45), (135, 32, 21), (136, 162, 181), (69, 40, 34), (50, 118, 86), (196, 91, 74), (145, 178, 150), (17, 94, 72), (232, 175, 164), (164, 143, 158), (107, 74, 78), (35, 60, 77), (180, 204, 177), (149, 20, 25), (66, 37, 40), (81, 148, 128), (21, 68, 60), (37, 66, 94), (23, 84, 90), (189, 88, 90), (69, 63, 57), (223, 176, 180)]
timmy.shape("turtle")
# colormode(255)
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)
number_of_dots=100  
for dot_count in range(1,number_of_dots+1):
    timmy.dot(20,random.choice(color_list))
    timmy.forward(50)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)
        timmy.setheading(0)
my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
