from turtle import Turtle

SCORE_HEIGHT = 200
SCORE_SIZE = 50

class Score (Turtle):
  def __init__(self):
    super().__init__()
    self._score_value = -1
    self.penup()
    self.speed("fastest")
    self.goto(0,SCORE_HEIGHT)
    self.hideturtle()
    self.color("yellow")
    self.increase_score()
  
  def increase_score(self):
    self.clear()
    self._score_value+=1
    self.write(self._score_value,move=False,align="center",font=("Arial", SCORE_SIZE, "normal"))