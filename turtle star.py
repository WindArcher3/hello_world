import turtle

#Window Setup

wn = turtle.Screen()
wn.title("Pong Game by Rastko Franovic")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0 | Player 2: 0", align= "center", font=("Corier", 24, "normal"))

#Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y = y + 20 
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y = y - 20 
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y = y +20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y = y - 20
    paddle_b.sety(y)

#Keyboard bindings 
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#variables
score_a = 0
score_b = 0


#Main game loop
while True:
    wn.update()
    #border checking 

    #Top and Buttom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1
    
    
    #Move the Ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Paddle and Ball collisions
    if (ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < paddle_a.ycor() + 50  and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx = ball.dx * -1
    elif (ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx = ball.dx * -1

    # right and Left
    if ball.xcor() > 350:
        pen.clear()
        score_a = score_a + 1
        pen.write("Player 1: {} | Player 2: {}".format(score_a,score_b),align="center", font =("Corier", 24, "normal"))
        ball.goto(0,0)
        ball.dx = ball.dx * -1

    if ball.xcor() < -350:
        pen.clear()
        score_b = score_b + 1
        pen.write("Player 1: {} | Player 2: {}".format(score_a,score_b),align="center", font =("Corier", 24, "normal"))
        ball.goto(0,0)
        ball.dx = ball.dx * -1








