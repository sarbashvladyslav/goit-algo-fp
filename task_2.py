
import turtle
import math

screen = turtle.Screen()

def create_turtle():
    t = turtle.Turtle()
    t.speed(0)
    t.color("red")
    t.pensize(2)
    return t

def start_position(t):
    t.penup()
    t.goto(0, -350)
    t.setheading(90)
    t.pendown()

def save_position(t):
    pos = t.position()
    heading = t.heading()
    return pos, heading

def new_position(t, pos, heading):
    t.penup()
    t.goto(pos)
    t.setheading(heading)
    t.pendown()

def pythagor(n):
    t = create_turtle()
    start_position(t)
    
    min_len = 40
    length = n * min_len
    angle = 45
    scale = math.sqrt(2) / 2
    
    def f(length):
        if length < min_len:
            return
        
        t.forward(length)

        pos, heading = save_position(t)

        t.left(angle)
        f(length * scale)

        new_position(t, pos, heading)
        
        t.right(angle)
        f(length * scale)
        
        new_position(t, pos, heading)

        t.backward(length)
        
    return f(length)

pythagor(6)

turtle.done()
