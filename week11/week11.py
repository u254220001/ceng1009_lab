# def fizz_buzz(n):
#     for i in range(1, n+1):
#         if i % 15 == 0:
#             print("fizzbuzz")
#         elif i % 3 == 0:
#             print("fizz")
#         elif i % 5 == 0:
#             print("buzz")
#
#         else:
#             print(i)
#
# fizz_buzz(25)


# def digit_sum(n):
#     total = 0
#     while n > 0:
#         total += n % 10
#         n //= 10
#         print(n)
#     return total
#
# print(digit_sum(1234))

# def alternate_case(s):
#     result = ""
#
#     for i in range(len(s)):
#         if i % 2 == 0:
#             result = result + s[i].upper()
#         else:
#             result = result + s[i].lower()
#     return result
#
# print(alternate_case("hello world!"))

# import turtle
# def draw_polygon(t, side, length):
#     for i in range(side):
#         t.forward(length)
#         t.left(360/side)
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# t = turtle.Turtle()
# t.pensize(3)
# colors = ["red", "yellow", "blue"]
#
# for i in range(3):
#     t.penup()
#     t.goto(-150 + i*120, 0)
#     t.pendown()
#     t.color(colors[i])
#     draw_polygon(t, i+3, 60)
#
# wn.exitonclick()

import turtle
# def filled_square(t,size,color):
#     t.fillcolor(color)
#     t.begin_fill()
#     for i in range(4):
#         t.forward(size)
#         t.left(90)
#     t.end_fill()
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# t = turtle.Turtle()
#
# for i in range(5):
#     t.penup()
#     t.goto(-165+ i * 70, -25)
#     t.pendown()
#     if i % 2 == 0:
#         filled_square(t,50,"red")
#     else:
#         filled_square(t,50,"blue")
#
#
# wn.exitonclick()

# def draw_square(t, size):
#     for i in range(4):
#         t.forward(size)
#         t.left(90)
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# t = turtle.Turtle()
# t.pensize(2)
#
# for i in range(12):
#     draw_square(t, 80)
#     t.left(30)
#
# wn.exitonclick()

# def draw_square(t, size, filled):
#     if filled:
#         t.begin_fill()
#     for i in range (4):
#         t.forward(40)
#         t.left(90)
#     if filled:
#         t.end_fill()
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# t = turtle.Turtle()
# size = 40
#
# for row  in range(6):
#     for col in range(6):
#         t.penup()
#         t.goto(-120 + col * size, -120 + row * size)
#         t.pendown()
#         draw_square(t, size, (row + col) % 2 == 0)
#
# wn.exitonclick()
