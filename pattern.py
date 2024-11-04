import turtle

# Setup
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.setup(width=600, height=600)

# Make turtle
maze_turtle = turtle.Turtle()
maze_turtle.hideturtle()
maze_turtle.speed(0)
maze_turtle.pensize(4)

# Draw the maze
def draw_maze():
# Outer walls
    maze_turtle.penup()
    maze_turtle.setpos(-200, -200)
    maze_turtle.pendown()
    maze_turtle.forward(400)
    maze_turtle.left(90)
    maze_turtle.forward(350)
    maze_turtle.left(90)
    maze_turtle.forward(400)
    maze_turtle.left(90)
    maze_turtle.forward(300)
    maze_turtle.left(90)

    # Internal walls 
    walls = [
        ((-150, -100), (-150, 150)), 
        ((-50, -200), (-50, 50)),   
        ((50, -90), (50, 100)),      
        ((100, -200), (100, 30)),     

        # Horizontal walls
        ((-150, 100), (-20, 100)),   
        ((-90, -50), (150, -50)),   
        ((-50, 0), (100, 0)),         
        ((-150, -150), (130, -150)),  

        # Walls 
        ((-100, 100), (-100, 0)),    
        ((-100, -100), (-100, -150)), 
        ((0, -100), (0, -150)),  

        # Pathways
        ((-150, -150), (-150, -200)), 
        ((-50, -150), (50, -150)),  
        ((50, 0), (100, 0)),         

        # Extra walls
        ((100, 90), (100, -70)),     
        ((200, 50), (200, -200)),   
    ]

    for start, end in walls:
        maze_turtle.penup()
        maze_turtle.goto(start)
        maze_turtle.pendown()
        maze_turtle.goto(end)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(1)
player.goto(-180, -180)  # Starting position

# Goal turtle
goal = turtle.Turtle()
goal.shape("circle")
goal.color("red")
goal.penup()
goal.goto(180, -180)  # Goal position

# Draw the maze
draw_maze()

def move_forward():
    navigator.forward(10)

def turn_left():
    navigator.left(90)

def turn_right():
    navigator.right(90)

screen = turtle.Screen()
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

turtle.mainloop()
