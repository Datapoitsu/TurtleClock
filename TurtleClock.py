import turtle
import math
import time

radius = 250
clockSegments = 360
clockBoardWidth = 5

markLenghts = [0.08,0.1] #percentage in decimal form
markWidths = [3,1]

#Hour, minute, second
handLenghts = [0.4,0.72,0.8] #percentage in decimal form
handWidhts = [10,6,4]
handColors = ["#000000","#000000","#FF0000"]

boardDrawer = turtle.Turtle()
handDrawer = turtle.Turtle()

def setup():
    boardDrawer.hideturtle()
    handDrawer.hideturtle()
    turtle.tracer(n = 1, delay=0.1)
    boardDrawer.speed(0)

def drawBoard():
    boardDrawer.penup()
    boardDrawer.pensize(clockBoardWidth)
    boardDrawer.setpos(radius,0)
    boardDrawer.setheading(90)
    boardDrawer.pendown()
    for i in range(clockSegments):
        boardDrawer.left(360 / clockSegments)
        boardDrawer.forward(2 * math.pi * radius / clockSegments)
    
def drawMarkers():
    for i in range(60):
        boardDrawer.penup()
        dist = markLenghts[math.ceil(i % 5 / 5)] * radius
        width = markWidths[math.ceil(i % 5 / 5)]
        boardDrawer.pensize(width)
        boardDrawer.setpos(math.cos(math.pi * 2 / 60 * i) * (radius - dist),math.sin(math.pi * 2 / 60 * i) * (radius - dist))
        boardDrawer.setheading(360 / 60 * i)
        boardDrawer.pendown()
        boardDrawer.forward(dist)

def drawArrows():
    handDrawer.clear() 
    handTime = [(time.localtime().tm_hour % 12 / 12.0),time.localtime().tm_min / 60.0,time.localtime().tm_sec / 60.0] #Time for all the arrows
    for i in range(len(handLenghts)):
        handDrawer.penup()
        handDrawer.setpos(0,0)
        handDrawer.setheading(90 - (360 * handTime[i]))
        handDrawer.color(handColors[i])
        handDrawer.pensize(handWidhts[i])
        handDrawer.pendown()
        handDrawer.forward(handLenghts[i] * radius)
    while(time.localtime().tm_sec / 60 == handTime[2]): #When time changes, we repeat the function
        time.sleep(1.0)
    drawArrows()

setup()
drawBoard()
drawMarkers()
drawArrows()