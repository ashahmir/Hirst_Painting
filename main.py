from turtle import Turtle, Screen
import random

rgb_colors = [(245, 241, 233), (227, 234, 242), (245, 234, 239), (233, 242, 236), (208, 158, 96), (234, 213, 101),
              (41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162), (148, 65, 83), (24, 40, 55),
              (204, 90, 68), (169, 159, 55), (139, 180, 152)]

django = Turtle()
screen = Screen()
screen.colormode(255)
django.hideturtle()
django.penup()
django.goto(-270, -200)
z = -200
for y in range(10):
    for x in range(10):
        django.penup()
        django.forward(50)
        django.dot(20, random.choice(rgb_colors))
    z += 50
    django.goto(-270, z)

screen.exitonclick()
