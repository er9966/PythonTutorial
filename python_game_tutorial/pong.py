import turtle
wn = turtle.Screen()
wn.title("Pong by Justina")
wn.bgcolor("black")
wn.setup(width=800, height=600)
# stop the window from updating, you can only manually update
# speed up the game
wn.tracer(0)

# Score
score_a = 0
score_b = 0


# Paddale A
paddle_a = turtle.Turtle() # Create a turtle object: module.Class()
paddle_a.speed(0)           # set speed of animation to max
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()            # don't draw a line when moving
paddle_a.goto(-350, 0)      # starts at left


# Paddle B
paddle_b = turtle.Turtle() # Create a turtle object: module.Class()
paddle_b.speed(0)          # set speed of animation to max
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()            # don't draw a line when moving
paddle_b.goto(350, 0)       # starts at left

# Ball
ball = turtle.Turtle() # Create a turtle object: module.Class()
ball.speed(0)          # set speed of animation to max
ball.shape("circle")
ball.color("white")
ball.penup()            # don't draw a line when moving
ball.goto(0, 0)         # starts at left
ball.dx = 2             # every time ball moves, move by 2 px
ball.dy = 2

# Create a scoring module, Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()        # we don't want to see the pen
pen.goto(0, 260)        # starts at this coordinate
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions: move paddles up and down
def paddle_a_up():      #define a funtion
    y = paddle_a.ycor() # need to know current y-coordinate of paddle a
    y += 20             # add 20px to y coordinate
    paddle_a.sety(y)    # set paddle to the new y

def paddle_a_down():      
    y = paddle_a.ycor() 
    y -= 20             
    paddle_a.sety(y)   

def paddle_b_up():      
    y = paddle_b.ycor() 
    y += 20             
    paddle_b.sety(y)     

def paddle_b_down():      
    y = paddle_b.ycor() 
    y -= 20             
    paddle_b.sety(y)  

# Keyboard binding
wn.listen()                    # tell screen to listen to keyboard input
wn.onkeypress(paddle_a_up, "w") # upon pressing w, call function
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up") 
wn.onkeypress(paddle_b_down, "Down")



# potatoes and meat of the game: main game loop
while True:
    wn.update()     # update the screen every loop

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border cheking for ball
    # compare the ball y-coord, once it gets to some point, bounces back
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1       # reverse the direction of ball once it hits the edge
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1       

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    # Paddle and ball collisions : comparing ball's coordinate with the paddles'
    # ball's x coordinate > paddle's x coordinate and ball's y coordinate is within the paddle y-coordinate range
    # edge case to take care of: what if ball is behind the paddle?
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1