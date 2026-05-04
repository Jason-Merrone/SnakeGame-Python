from collections import deque
import copy
from turtle import Turtle


STARTING_POS = [(-40,0), (-20,0), (0,0)]
MOVE_DISTANCE = 20

class Snake:

  def __init__(self):
    self.segments = deque()
    self._create_snake()
    self._head = self.segments[-1]

    self._dir = "right"
    self._vertical = {"up","down"}
    self._horizontal = {"left","right"}
  
  def _create_snake(self):
    for i in range(len(STARTING_POS)):
      new_segment = Turtle(shape="square")
      new_segment.color("white")
      new_segment.penup()
      new_segment.goto(STARTING_POS[i])
      self.segments.append(new_segment)
    
  def move(self):
    self.segments[0].goto(self._head.position())
    self.segments[0].setheading(self._head.heading())
    self.segments.append(self.segments.popleft())
    self._head = self.segments[-1]
    self._head.forward(MOVE_DISTANCE)
  
  def up(self):
      if self._dir in self._horizontal:
         self._head.setheading(90)
         self._dir = "up"

  def down(self):
      if self._dir in self._horizontal:
         self._head.setheading(270)
         self._dir = "down"

  def left(self):
      if self._dir in self._vertical:
         self._head.setheading(180)
         self._dir = "left"

  def right(self):
      if self._dir in self._vertical:
         self._head.setheading(0)
         self._dir = "right"