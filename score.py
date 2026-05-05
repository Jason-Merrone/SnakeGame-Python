from turtle import Turtle
from highscore import HighScore
SCORE_HEIGHT = 270
SCORE_SIZE = 10

class Score (Turtle):
  def __init__(self):
    super().__init__()
    self._score_value = -1
    self._high_score = HighScore()
    self.penup()
    self.speed("fastest")
    self.goto(0,SCORE_HEIGHT)
    self.hideturtle()
    self.color("yellow")
    self.increase_score()
  
  def increase_score(self):
    self._score_value+=1
    self.update_screen()
  
  def update_screen(self):
    self.clear()
    self.write(f"Score: {self._score_value}                   High Score: {self._high_score.high_score}",move=False,align="center",font=("Arial", SCORE_SIZE, "normal"))
  
  def update_high_score(self):
    self._high_score.update(self._score_value)
    self.update_screen()
