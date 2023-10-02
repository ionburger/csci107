import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor("grey")
t.color("yellow")
t.fillcolor("black")
t.hideturtle()
t.shape("arrow")

t.up()
t.goto(-140,-35)

t.down()
rectl = 280
rectw = 70
t.begin_fill()
t.fd(rectl)
t.lt(90)
t.fd(rectw)
t.lt(90)
t.fd(rectl)
t.lt(90)
t.fd(rectw)
t.end_fill()

t.fillcolor("yellow")
t.up()
t.goto(-140,-0)
t.lt(90)
for i in range(7):
    t.fd(35)
    t.stamp()

turtle.mainloop()