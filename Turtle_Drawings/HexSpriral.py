#HexSpiral.py
import turtle

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("HexSpiral")

#I don't know
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
t = turtle.Turtle()
t.speed(0)
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)

delay = input("Press enter to finish")