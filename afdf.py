import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("red")
t.color("black","white")
t.hideturtle()
t.pensize(3)
t.shape("turtle")
t.shapesize(3)

t.up()
t.goto(-75,-75)
t.down()

t.begin_fill()
for i in range(4):
    t.fd(150)
    t.lt(90)

t.end_fill()
t.up()
t.goto(0,0)
t.down()

t.color("black")
#t.seth(90)
t.stamp()


s.exitonclick()