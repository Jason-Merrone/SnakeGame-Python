from collections import deque
from turtle import Turtle


STARTING_POS = [(-40,0), (-20,0), (0,0)]
MOVE_DISTANCE = 20

class Snake:

  def __init__(self):
    self.segments = deque()
    self._body_set = set() # This is for efficiently checking is the apple collides with the snake body during generation
    self._create_snake()
    self._head = self.segments[-1]

    self._curr_dir = "right"
    self._prev_dir = "right"
    self._vertical = {"up","down"}
    self._horizontal = {"left","right"}
    self._extend = False
  
  def _create_snake(self):
    for i in range(len(STARTING_POS)):
      new_segment = Turtle(shape="square")
      new_segment.color("white")
      new_segment.penup()
      new_segment.goto(STARTING_POS[i])
      self.segments.append(new_segment)
      if i != len(STARTING_POS)-1:
        self._body_set.add((int(new_segment.xcor()), int(new_segment.ycor())))
    
  def move(self):
    if not self._extend:
      tail = self.segments[0]
      self._body_set.remove((int(tail.xcor()), int(tail.ycor())))
      tail.goto(self._head.position())
      tail.setheading(self._head.heading())

      self.segments.popleft()
    else:
      tail = self._head.clone()
      self._extend = False

    self._body_set.add((int(self._head.xcor()), int(self._head.ycor())))

    self.segments.append(tail)
    self._head = self.segments[-1]
    self._head.forward(MOVE_DISTANCE)
    self._prev_dir = self._curr_dir

    if self.collide_with_body(self._head):
       return False
    return True
  
  def up(self):
      if self._prev_dir in self._horizontal:
         self._head.setheading(90)
         self._curr_dir = "up"

  def down(self):
      if self._prev_dir in self._horizontal:
         self._head.setheading(270)
         self._curr_dir = "down"

  def left(self):
      if self._prev_dir in self._vertical:
         self._head.setheading(180)
         self._curr_dir = "left"

  def right(self):
      if self._prev_dir in self._vertical:
         self._head.setheading(0)
         self._curr_dir = "right"
  
  def collide_with_apple(self,apple):
     if self._head.distance(apple) < 5:
        self._extend = True
        apple.refresh(self)
  
  def collide_with_body(self,other):
     return (int(other.xcor()), int(other.ycor())) in self._body_set