from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)

screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # Turn off the animation delay

game_is_on = True

snake = Snake()

# Keypress logic
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
  screen.update()
  time.sleep(.1)

  snake.move()

screen.exitonclick()