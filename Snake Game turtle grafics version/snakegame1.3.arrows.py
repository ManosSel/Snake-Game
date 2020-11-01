from turtle import Screen,Turtle
from time import sleep
from random import randint

window=Screen() # Creating the Screen object where turtle are drawn on
window.setup(500,600)  # Initialising window's size
window.bgcolor("green") # Setting green as the background color
window.title("Snake Game") # Renaming window 

snake = Turtle() # Head of the snake
snake.shape("square") # Setting the shape square, the color blue, the starting direction stop, the size smaller than the default 
snake.color("blue") 
snake.shapesize(0.8)
snake.direction="stop" # Theis property will help for the movement of the snake
snake.penup()
snake.speed(0)


apple = Turtle() # Snake's food
apple.shape("circle") # Setting the shape circle, the color red, the size smaller than the default 
apple.penup()
apple.shapesize(0.6)
apple.color("red")
apple.speed(0)

pen = Turtle() # The pen for the score writing 
pen.speed(0) # Setting the color white and hiding the turtle  
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)

def movement():
    ''' Moves the snake in the direction that it has '''
    if snake.direction == "up":
        snake.sety(snake.ycor() + 20)
    if snake.direction == "down":
        snake.sety(snake.ycor() - 20)
    if snake.direction == "right":
        snake.setx(snake.xcor() + 20)
    if snake.direction == "left":   
        snake.setx(snake.xcor() - 20)

# These set of function will be call when buttons are pressed and will change the direction of the snake
def go_up():
    snake.direction = "up"
def go_down():
    snake.direction = "down"
def go_right():
    snake.direction = "right"
def go_left():
    snake.direction = "left"

parts = [snake] # The list with the pieces of the snake , the first piece is the head
orone = 0

border = Turtle() # The creation of the board graphics
border.penup()
border.speed(0)
border.pensize(10)
border.goto(-232,232)
border.pendown() 
for i in range(4): # Making o square
    border.forward(464)
    border.right(90)

score = 0 # Initializing score and highscore
high = 0

while True:
    apple.goto(0,100)
    pen.write(f"Score:   {score}   High Score:   {high} ",align="center",font=("carrier",26,"normal")) # Writing the current score
    game_running = True # Setting the game flag to True

    while game_running:
        window.update() # Window listens to the keyboard
        window.listen() 

        window.onkey(go_up,"Up") # Binding the move functions to the arrows
        window.onkey(go_down,"Down")
        window.onkey(go_right,"Right")
        window.onkey(go_left,"Left")

        # Lose if the snake hits the borders
        if snake.xcor()>200 or snake.xcor()<-200 or snake.ycor()>200 or snake.ycor()<-200:
            snake.direction="stop"
            game_running = False

        # Snake and apple collision 
        if snake.distance(apple)<15: 
            apple.goto(randint(-200,200),randint(-200,200)) # Moving the apple to a new random position

            score += 10 # Add 10 points
            if score > high: # Changing the highscore if the score is bigger than it 
                high = score
            pen.clear() # Updating the score in the screen
            pen.write(f"Score:   {score}   High Score:   {high} ",align="center",font=("carrier",26,"normal"))

            body = Turtle() # Making a new part of the snake
            body.shape("square") # Same settings as the head of the snake 
            body.color("blue")
            body.shapesize(0.8)
            body.speed(0)
            body.penup()
            body.goto(snake.xcor(),snake.ycor()) # Going to the position of the haed snake
            parts.append(body)

        for part_index in range(len(parts)-1,0,-1): # The whole body from the last part to the first by index
            x1 = parts[part_index-1].xcor() # Updating the position of the part
            y1 = parts[part_index-1].ycor()
            parts[part_index].goto(x1,y1)

        # Eating yourself
        for i in range(2,len(parts)): # All the part of the snake minus the first and the second 
            if snake.distance(parts[i])<15:
                snake.direction = "stop"
                game_running = False # End the game

        movement() # Move the head
        sleep(0.05) # Small delay

    score = 0 # Reseting the game
    pen.clear()
    snake.goto(0,0)
    
    for part in parts[1:]: # Hiding all the parts of the turle
        part.hideturtle()
    del parts[1:] # Clearing the list of the parts except of the snake

    sleep(0.2)


