import turtle

def draw_square(any_turtle):
    for i in range(4):
        any_turtle.forward(100)
        any_turtle.right(90)

def draw_something():
    window = turtle.Screen()
    window.bgcolor("aqua")

    ## draw brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range(1, 36):

        draw_square(brad)
        brad.right(10)
    window.exitonclick()

def draw_initials():
    window = turtle.Screen()
    window.bgcolor("aqua")
    paul = turtle.Turtle()

    ##draw P
    
    paul.penup()
    paul.goto(0,0)
    paul.pendown()
    paul.goto(0,100)
    paul.penup()
    paul.goto(27,60)
    paul.pendown()
    paul.circle(30)

    ##draw V
    paul.penup()
    paul.goto(60,0)
    paul.pendown()
    paul.left(110)
    paul.forward(170)
    paul.penup()
    paul.goto(60,0)
    paul.pendown()
    paul.right(40)
    paul.forward(110)
    paul.penup()
    paul.goto(110,10)

    window.exitonclick()


    ## draw angie
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")

    #angie.circle(100)

    #draw bob
    #bob = turtle.Turtle()
    #bob.shape("turtle")
    #bob.color("green")
    #bob.speed(2)

    #for j in range(3):
       # bob.forward(60)
        #bob.right(120)





draw_initials()


