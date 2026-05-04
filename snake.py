from turtle import Turtle


STARTING_POS = [(0,0), (-20,0), (-40,0)]

class Snake:

  def __init__(self):
    self.segments = []
    self.create_snake()
  
  def create_snake(self):
    for pos in STARTING_POS:
      new_segment = Turtle(shape="square")
      new_segment.color("white")
      new_segment.penup()
      new_segment.goto(pos)
      self.segments.append(new_segment)
    
  def move(self):
    for i in range(len(self.segments)-1, 0, -1):
      self.segments[i].goto(self.segments[i-1].position())
    self.segments[0].forward(20)