import turtle
import math

screen = turtle.Screen()
screen.bgcolor("green")
t = turtle.Turtle()
t.speed(0)

def draw_circle(radius, color):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_petal(radius, angle, color):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)
    t.end_fill()

def draw_flower(petal_count, radius, angle, color):
    for _ in range(petal_count):
        draw_petal(radius, angle, color)
        t.right(360 / petal_count)


def draw_overlapping_flowers():
    t.penup()  
    t.goto(0, 0)  
    t.pendown()  

  
    draw_flower(10, 120, 60, "red")  

    
    draw_flower(8, 90, 60, "yellow")  

    
    draw_flower(6, 60, 60, "red")  

    
    draw_flower(6, 30, 60, "white") 

def draw_circle_ring(radius, circle_radius, count, color):
    t.penup()
    for i in range(count):
        angle = 360 / count * i
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        t.goto(x, y - circle_radius)
        t.pendown()
        t.color(color)
        t.begin_fill()
        t.circle(circle_radius)
        t.end_fill()
        t.penup()


def draw_concentric_circles():
    draw_circle(258,"purple")
    draw_circle(255,"floralwhite")
    draw_circle(250,"darkred")
    draw_circle_ring(200,20 ,30,"white")
    draw_circle(200, "gold")  

    draw_circle_ring(150,20,30,"purple")
    
    draw_circle(150, "darkorange")  

    draw_circle_ring(100, 20,20,"pink")

    draw_circle(100, "purple") 


draw_concentric_circles()  
draw_overlapping_flowers()  

t.hideturtle()
turtle.done()
