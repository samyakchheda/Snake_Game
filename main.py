
from turtle import Screen
import time
from snake import Snake

snake=Snake()
screen=Screen()
screen.tracer()
screen.screensize(canvwidth=500,canvheight=500,bg="black")
screen.title("Snake Game")

screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Left,"Left")
screen.onkey(snake.Right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    #time.sleep(0.01)
    snake.move()


    #Detect collision with food
    snake.foodCollision()
    if snake.wallCollision():
        game_is_on=False
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment)<10:
             game_is_on=False
             snake.tailCollision()








screen.exitonclick()
