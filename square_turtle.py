import turtle
screen = turtle.Screen()
screen.bgcolor("lightblue")
t = turtle.Turtle()
t.color("purple")         
t.pensize(3)                 
t.speed(3)
for _ in range(4):
    t.forward(150)           
    t.right(90)
screen.mainloop()
turtle.done()