import random
from turtle import Turtle


class Apple (Turtle):
  def __init__(self,snake, screen_width:int, screen_height:int):
    super().__init__()
    self.shape("square")
    self.penup()
    self.color("red")
    self.speed("fastest") # Don't need to watch turtle be created
    self.refresh(snake)

  def refresh(self, snake):
    while True:
      random_x = random.randrange(-280, 281, 20)
      random_y = random.randrange(-280, 281, 20)
      self.goto(random_x,random_y)

      if not snake.collide_with_body(self):
        break