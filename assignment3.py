import turtle

c = turtle.Screen()
c.setup(width=500, height=500)

pixels = 
t = turtle.Turtle()
t.hideturtle()
t.speed(10)

t.penup()
t.goto(200, 200)
t.pendown()

for i in range(4):
    t.right(90)
    t.forward(400)

for i in range(16):
    t.left(90)
    t.forward(400)
turtle.done()