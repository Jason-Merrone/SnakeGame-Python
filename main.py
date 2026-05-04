from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600,height=600)

screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # Turn off the animation delay

starting_positions = [(0,0), (-20,0), (-40,0)]

segments = []

for pos in starting_positions:
  new_segment = Turtle(shape="square")
  new_segment.color("white")
  new_segment.penup()
  new_segment.goto(pos)
  segments.append(new_segment)

game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(.5)

  for i in range(len(segments)-1, 0, -1):
    segments[i].goto(segments[i-1].position())
  segments[0].forward(20)

screen.exitonclick()