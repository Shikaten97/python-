import turtle
tom = turtle.Turtle()
tom.shape('turtle')
tom.color('gray')
tom.speed(0)
tom.left(45)

for count in range (100):
  for g in range(3):
    tom.fd(100)
    tom.left(120)
  tom.right(360.0/100)

tom.color('blue')
for c in range(100):
  tom.circle(25)
  tom.left(360.0/100)
tom.color('black')
for c in range(100):
  tom.circle(10)
  tom.left(360.0/100)
tom.pu()
tom.goto(300,0)
tom.pd()

tom.color('gray')
for count in range (100):
  for g in range(3):
    tom.fd(100)
    tom.left(120)
  tom.right(360.0/100)

tom.color('blue')
for c in range(100):
  tom.circle(25)
  tom.left(360.0/100)
tom.color('black')
for c in range(100):
  tom.circle(10)
  tom.left(360.0/100)