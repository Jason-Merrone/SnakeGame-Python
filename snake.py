from collections import deque
from turtle import Turtle
from apple import Apple


STARTING_POS = [(-40,0), (-20,0), (0,0)]
MOVE_DISTANCE = 20

class Snake:

  def __init__(self, screen_width:int, screen_height:int):
    self.segments = deque()
    self._body_set = set() # This is for efficiently checking if the apple collides with the snake body during generation
    self._create_snake()
    self._head = self.segments[-1]
    self._screen_width = screen_width
    self._screen_height = screen_height

    self._curr_dir = "right"
    self._prev_dir = "right"
    self._vertical = {"up","down"}
    self._horizontal = {"left","right"}
    self._extend = False
  
  def _create_snake(self):
    for i in range(len(STARTING_POS)):
      new_segment = Turtle(shape="square")
      new_segment.color("green")
      new_segment.penup()
      new_segment.goto(STARTING_POS[i])

      self.segments.append(new_segment)

      if i != len(STARTING_POS)-1:
        self._body_set.add((int(round(new_segment.xcor())), int(round(new_segment.ycor()))))
    
  def move(self):
    if not self._extend:
      tail = self.segments[0]
      self._body_set.remove((int(round(tail.xcor())), int(round(tail.ycor()))))
      tail.goto(self._head.position())
      tail.setheading(self._head.heading())

      self.segments.popleft()
    else:
      tail = self._head.clone()
      self._extend = False

    self._body_set.add((int(round(self._head.xcor())), int(round(self._head.ycor()))))

    self.segments.append(tail)
    self._head = self.segments[-1]
    self._head.forward(MOVE_DISTANCE)
    self._prev_dir = self._curr_dir

    if self.collide_with_body(self._head) or self._collide_with_wall():
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
  
  def collide_with_apple(self,apple:Apple) -> bool:
    if self._head.distance(apple) < 5:
      self._extend = True
      apple.refresh(self)
      return True
    return False
  
  def collide_with_body(self,other:Turtle) -> bool:
    return (int(round(other.xcor())), int(round(other.ycor()))) in self._body_set
  
  def _collide_with_wall(self) -> bool:
    return self._head.xcor() > self._screen_width/2-1 or self._head.xcor() < -self._screen_width/2+1 or self._head.ycor() > self._screen_height/2-1 or self._head.ycor() < -self._screen_height/2+1
