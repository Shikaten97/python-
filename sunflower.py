import turtle
tom = turtle.Turtle()
tom.shape('turtle')
tom.color('white','yellow')
tom.speed(0)
#tom.tracer(10)
c=40
d=100
u=40

tom.begin_fill()
for A in range (c):
    tom.circle(100,90)
    tom.pu()
    tom.goto(0,0)
    tom.pd()
    tom.left(360.0/c)
tom.end_fill()
tom.color('brown')
for B in range (d):
    tom.circle(30,90)
    tom.goto(0,0)
    tom.left(360.0/d)
x=300
for H in range (u):
    tom.penup()
    tom.goto(0,0)
    tom.setheading(0)
    tom.rt(90)
    tom.fd(120)
    tom.left(360.0/u)
    tom.pendown()
    tom.color('dark green')
    tom.circle(x,45)
    x=x+2