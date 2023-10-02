import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("lightgreen")
t.color("darkblue")
t.shape("turtle")
t.pensize(3)
t.hideturtle()
t.speed("fastest")

t.stamp()

for i in range(12):
    t.lt(30)
    t.up()
    t.fd(100)
    t.down()
    t.fd(10)
    t.up()
    t.fd(10)
    t.stamp()
    t.goto(0,0)
t.pencolor("red")
t.pensize(1)
for i in range(60):
    t.lt(6)
    t.up()
    t.fd(80)
    t.down()
    t.fd(10)
    t.up()
    t.goto(0,0)


turtle.mainloop()

