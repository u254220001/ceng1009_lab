# import random
#
# for i in range(10):
#     print(random.random())


# import random
#
# for i in range(10):
#     print(random.randint(25,35))

# import math
#
# # hypotenuse = math.hypot(3,4)
# # print(hypotenuse)
#
# a = int(input("Enter length: "))
# b = int(input("Enter width: "))
# hypotenuse = math.sqrt(a**2 + b**2)
#
# print(hypotenuse)


# import math
# def areaOfCircle(radius):
#     area = math.pi * (radius ** 2)
#     return area
# print(areaOfCircle(5))

# import turtle
#
# def drawStar(t, side):
#     for i in range(5):
#         t.forward(side)
#         t.right(144)
#
# screen = turtle.Screen()
# tess = turtle.Turtle()
#
# drawStar(tess, 100)
#
# screen.exitonclick()


# def drawSquare(t, side):
#     for i in range(4):
#         t.forward(side)
#         t.left(90)
#
# import turtle
#
# tess = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("Lightgreen")
# tess.color("pink")
# tess.pensize(3)
#
# for i in range(5):
#     drawSquare(tess, 20)
#     tess.penup()
#     tess.forward(40)
#     tess.pendown()
#
# screen.exitonclick()

# import turtle
#
# screen = turtle.Screen()
# tess = turtle.Turtle()
# screen.bgcolor("Lightgreen")
# tess.color("red")
# tess.pensize(3)
#
# for i in range(20, 120, 20):
#     drawSquare(tess, i)
#     tess.penup()
#     tess.backward(10)
#     tess.right(90)
#     tess.forward(10)
#     tess.left(90)
#     tess.pendown()
#
# screen.exitonclick()
