import random
tom = Turtle()
tom.shape('turtle')
tom.color('white','yellow')
tom.speed(0)
#tom.tracer(10)
mus=40
zub=100
m3rs=40

tom.begin_fill()
for t3mus in range (mus):
    tom.circle(100,90)
    tom.pu()
    tom.goto(0,0)
    tom.pd()
    tom.left(360.0/mus)
tom.end_fill()
tom.color('brown')
for zobie in range (zub):
    tom.circle(30,90)
    tom.goto(0,0)
    tom.left(360.0/zub)
x=300
for ku3al in range (m3rs):
    tom.penup()
    tom.goto(0,0)
    tom.setheading(0)
    tom.rt(90)
    tom.fd(120)
    tom.left(360.0/m3rs)
    tom.pendown()
    tom.color('dark green')
    tom.circle(x,45)
    x=x+2




