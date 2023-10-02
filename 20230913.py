import turtle
canvas = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
t.speed(10)

if (input("fill (y/n): ")) == "y" or "yes":
    print("filling")
    t.begin_fill()

def color():
    try:
        t.color(input("what color: "))
    except turtle.TurtleGraphicsError:
        print("invalid color")
        color()

color()
l = int(input("what length sides: "))
s = (input("how many sides or name of shape: "))
#if type(s) == str:
#    s = 
for i in range(s):
    t.forward(l)
    t.left(360/s)
t.end_fill()
turtle.done()
