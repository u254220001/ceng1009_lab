# Exercise 1

# def sumTo(n):
#     total = n * (n + 1) /2
#     return total
#
# print(sumTo(10))
#
# n = int(input("Please enter a number: "))
# print("Sum is", sumTo(n))

# Exercise 2

# import turtle
#
# def drawStar(t, n, size):
#     angle = 180 - 180 /n
#     for i in range(n):
#         t.forward(size)
#         t.right(angle)
#
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.pensize(3)
#
# drawStar(t, 11, 100)
# wn.exitonclick()

# Exercise 3

# def sumTo(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#     return total
#
# print(sumTo(10))
# n = int(input("Enter a number: "))
# print("Sum is: ", sumTo(n))

# Exercise 4

# import math
#
# def mySqurt(x):
#     quess = x / 2
#     for i in range(20):
#         quess = (1/2) * (quess + x / quess)
#
#     return quess
#
# n = int(input("Enter a positive integer: "))
#
# print("The result is",mySqurt(n))
# print("The result is",math.sqrt(n))

# Exercise 5

# import turtle
# def drawSprite(someturtle, legs, length):
#     angle = 360 / legs
#     for i in range(legs):
#         someturtle.forward(length)
#         someturtle.backward(length)
#         someturtle.left(angle)
#
# def fancySquare(t, size):
#
#     for i in range(4):
#        drawSprite(t, 8, 20)
#        t.forward(size)
#        t.left(90)
#
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.color("pink")
# t.speed(6)
# t.pensize(2)
#
# fancySquare(t, 100)
# wn.exitonclick()

# Exercise 6

# def checkSign(x):
#     if number > 0:
#         return "the number is positive"
#     elif number < 0:
#         return "the number is negative"
#     else:
#         return "the number is zero"
#
# numbers = [-7, 5, 0]
#
# for number in numbers:
#     print(number, checkSign(number))

# Exercise 7

import turtle

def drawBar(t, height, gap):
    t.penup()
    t.left(90)
    t.forward(height+ gap)
    t.write("" + str(height))
    t.backward(height + gap)
    t.right(90)
    t.pendown()

    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

def barChart(data):
    maxheight = max(data)
    num_bars = len(data)
    border = 10

    gap = (maxheight - border) / 25

    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    right = 40 x num_bars + border
    top = maxheight + 4 x border

    wn.setworldcoordinates(-border, -border, right, top)
    