import turtle

wn = turtle.Screen()
wn.title("Rules of the road by Rastko")
wn.bgcolor("gray")
wn.setup(width=1600,height=1000)
wn.tracer(0)

#Python program to draw car in turtle programming
 
# Import required library
import turtle
  
   
car = turtle.Turtle()

# sidewalk 1
sidewalk_1 = turtle.Turtle()
sidewalk_1.speed(0)
sidewalk_1.shape("square")
sidewalk_1.color("white")
sidewalk_1.shapesize(stretch_wid = 7, stretch_len = 800)
sidewalk_1.penup()
sidewalk_1.goto(0,500)

# sidewalk 2
sidewalk_2 = turtle.Turtle()
sidewalk_2.speed(0)
sidewalk_2.shape("square")
sidewalk_2.color("white")
sidewalk_2.shapesize(stretch_wid = 7, stretch_len = 800)
sidewalk_2.penup()
sidewalk_2.goto(0,-400)

# median strip
med_strp = turtle.Turtle()
med_strp.speed(0)
med_strp.shape("square")
med_strp.color("yellow")
med_strp.shapesize(stretch_wid = 2, stretch_len = 800)
med_strp.penup()
med_strp.goto(0,0)

#car hood

car_hood = turtle.Turtle()
car_hood.speed(0)
car_hood.shape("square")
car_hood.color("white")
car_hood.shapesize(stretch_wid = 3, stretch_len=15)
car_hood.penup()
car_hood.goto(0,100)

#car body

car_body = turtle.Turtle()
car_body.speed(0)
car_body.shape("square")
car_body.color("red")
car_body.shapesize(stretch_wid = 5, stretch_len=25)
car_body.penup()
car_body.goto(10,25)
 
# tire 1
ball_1 = turtle.Turtle()
ball_1.speed(0)
ball_1.shape("circle")
ball_1.color("black")
ball_1.shapesize(stretch_wid = 5, stretch_len=5)
ball_1.penup()
ball_1.goto(-150, 0)
ball_1.dx = 0.2
ball_1.dy = 0.2

# tire 2
ball_2 = turtle.Turtle()
ball_2.speed(0)
ball_2.shape("circle")
ball_2.color("black")
ball_2.shapesize(stretch_wid = 5, stretch_len=5)
ball_2.penup()
ball_2.goto(150, 0)
ball_2.dx = 0.2
ball_2.dy = 0.2


#Functions
def car_up():
    y = car_hood.ycor()
    y = y + 25 
    car_hood.sety(y)

    y1 = car_body.ycor()
    y1 = y1 + 25 
    car_body.sety(y1)

    y2 = ball_1.ycor()
    y2 = y2 + 25
    ball_1.sety(y2)

    y3 = ball_2.ycor()
    y3 = y3 + 25
    ball_2.sety(y3)

def car_down():
    y = car_hood.ycor()
    y = y - 25 
    car_hood.sety(y)

    y1 = car_body.ycor()
    y1 = y1 - 25
    car_body.sety(y1)

    y2 = ball_1.ycor()
    y2 = y2 - 25
    ball_1.sety(y2)

    y3 = ball_2.ycor()
    y3 = y3 - 25
    ball_2.sety(y3)

def car_backward():
    x = car_hood.xcor()
    x = x + 25 
    car_hood.setx(x)

    x1 = car_body.xcor()
    x1 = x1 + 25 
    car_body.setx(x1)

    x2 = ball_1.xcor()
    x2 = x2 + 25 
    ball_1.setx(x2)

    x3 = ball_2.xcor()
    x3 = x3 + 25
    ball_2.setx(x3)

def car_forward():
    x = car_hood.xcor()
    x = x - 25 
    car_hood.setx(x)

    x1 = car_body.xcor()
    x1 = x1 - 25 
    car_body.setx(x1)

    x2 = ball_1.xcor()
    x2 = x2 - 25 
    ball_1.setx(x2)

    x3 = ball_2.xcor()
    x3 = x3 - 25
    ball_2.setx(x3)

#Keyboard bindings 
wn.listen()
wn.onkeypress(car_up, "w")
wn.onkeypress(car_down, "s")
wn.onkeypress(car_backward, "d")
wn.onkeypress(car_forward, "a")

while True:
    wn.update()




































































































































































